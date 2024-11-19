from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from .models import GameRecord, Movie
from .game_logic import play_game_round, generate_game_summary
from .serializers import MovieSerializer, GameRecordSerializer
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def test(request):
    # id=1인 Movie 객체 가져오기 (일단 1로 시험해보고 나중에 로그인한 사용자로 바꿔보자.)
    try:
        movie = Movie.objects.get(id=6) # 일단 1
    except Movie.DoesNotExist:
        return Response({"error": "Movie not found"}, status=404)
    # 직렬화
    serializer = MovieSerializer(movie)   
    return Response(serializer.data)


@api_view(['POST'])
def start_game(request):
    movie_id = request.data.get('movie_id')
    print(movie_id)
    print('gggg')
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response({"error": "Movie not found"}, status=404)
    
    User = get_user_model()         # 유저모델에서
    user = User.objects.get(id=6)   # 여기도 일단 1번 유저 가져옴.
    
    game_record = GameRecord.objects.create(
        movie = movie, 
        user = user ,
        history = '[]', 
        total_score=0
    )
    initial_question = movie.initial_questions.order_by('?').first()
    
    if not initial_question:
        return Response({"error": "No initial questions available for this movie."}, status=400)

    return Response({
        'game_id': game_record.id,
        'initial_question': initial_question.question
    })


@api_view(['POST'])
def play_game(request, game_id):
    game_record = GameRecord.objects.get(id=game_id)
    user_action = request.data.get('user_action')
    next_problem, is_game_over = play_game_round(game_record, user_action)
    
    response_data = {
        'next_problem': next_problem,
        'is_game_over': is_game_over,
        'total_score': game_record.total_score
    }
    
    if is_game_over:
        summary = generate_game_summary(game_record)
        response_data['summary'] = summary
    
    return Response(response_data)

@api_view(['GET'])
def get_game_summary(request, game_id):
    game_record = GameRecord.objects.get(id=game_id)
    summary = generate_game_summary(game_record)
    return Response({
        'summary': summary,
        'total_score': game_record.total_score
    })