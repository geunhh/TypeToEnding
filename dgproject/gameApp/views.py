from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.response import Response
from .models import GameRecord, Movie, Comment
from .game_logic import play_game_round, generate_game_summary, anlayze_result
from .serializers import (
    MovieSerializer,
    GameRecordSerializer,
    InitialQuestionSerializer,
    CommentSerializer,
)
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
import pprint
import json


@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def movielist(request):
    if request.method == "GET":
        """
        전체 영화 목록을 반환하는 API

        Returns:
            Response: 직렬화된 영화 데이터 목록
        """
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        """
        영화 생성하는 API

        """
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {"status": "error", "message": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def test(request):
    """
    게임 기록 테스트용 API

    Returns:
        Response: 전체 게임 기록 데이터
    """
    try:
        gamerecords = GameRecord.objects.all()
    except GameRecord.DoesNotExist:
        return Response({"error": "gamerecord not found"}, status=404)
    # 직렬화
    serializer = GameRecordSerializer(gamerecords, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def start_game(request):
    """
    새로운 게임을 시작하는 API
    Args:
        request: movie_id를 포함한 요청 객체

    Returns:
        Response: 생성된 게임 ID와 초기 질문
    """

    movie_id = request.data.get("movie_id")
    print(movie_id)
    print("gggg")
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

    user = user = request.user
    
    # 랜덤 질문 가져오기
    initial_question = movie.initial_questions.order_by("?").first() # order_by("?") : 쿼리셋 결과를 랜덤하게 섞어서 반환



    # 게임 레코드 생성.
    game_record = GameRecord.objects.create(
        movie=movie,
        user=user,
        history=[
            {
                "round": 0,
                "situation": initial_question.question,
                "user_action": None,
                "score": 0,
                "next_situation": initial_question.question,  # 초기 상황에 next_situation 추가
            }
        ],
        total_score=0,
    )

    # 초기 질문이 없는 경우
    if not initial_question:
        return Response(
            {"error": "No initial questions available for this movie."}, status=status.HTTP_400_BAD_REQUEST
        )
    
    # 리턴 해주기
    return Response(
        {
            "game_id": game_record.id,
            "initial_question": initial_question.question,
        }
    )


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def play_game(request, game_id):
    """
    게임 진행을 처리하는 API

    Args:
        request: 사용자 행동이 포함된 요청 객체
        game_id: 진행할 게임의 ID

    Returns:
        Response: 다음 문제, 게임 종료 여부, 총점, 평가 이유, 유효성 여부
    """
    # 기존에 진행했던 게임 데이터 찾음.
    game_record = GameRecord.objects.get(
        id=game_id
    )  
    # user_acton. 작성한 시나리오 가져옴.
    user_action = request.data.get("user_action")  

    # 게임 record와 작성한 시나리오 던지기
    next_problem, is_game_over, reason, is_valid = play_game_round(
        game_record, user_action
    )

    # 반환 데이터 생성.
    response_data = {
        "next_problem": next_problem,
        "is_game_over": is_game_over,
        "total_score": game_record.total_score,
        "reason": reason,
        "is_valid": is_valid,
    }

    # 게임 종료 시
    if is_game_over:
        summary = generate_game_summary(game_record)
        response_data["summary"] = summary

    return Response(response_data,status=status.HTTP_200_OK)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_game_summary(request, game_id):
    """
    게임 요약을 조회하는 API

    Args:
        request: 요청 객체
        game_id: 조회할 게임의 ID

    Returns:
        Response: 게임 요약과 총점
    """
    game_record = GameRecord.objects.get(id=game_id)
    summary = generate_game_summary(game_record)
    return Response({"summary": summary, "total_score": game_record.total_score},status=status.HTTP_200_OK)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_movie(request, game_id):
    """
    게임 히스토리를 조회하는 API

    Args:
        request: 요청 객체
        game_id: 조회할 게임의 ID

    Returns:
        Response: 게임 진행 기록
    """
    game_record = GameRecord.objects.get(id=game_id)
    return Response({"history": game_record.history},status=status.HTTP_200_OK)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def recommend_movie(request, game_id):
    # print(request.data)
    data = request.data
    """
        추천을 위한 파싱.
    """
    history = data.get("result", {}).get("history", [])
    # pprint.pprint(history[5])

    result = anlayze_result(
        history[1], history[2], history[3], history[4], history[5], game_id
    )

    return Response({"result": result},status=status.HTTP_200_OK)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user_game_record(request, user_id):
    """
    특정 사용자의 게임 기록을 조회하는 API

    Args:
        request: 요청 객체
        user_id: 조회할 사용자의 ID

    Returns:
        Response: 해당 사용자의 게임 기록 목록
    """
    # 주어진 user_id에 해당하는 게임 기록 필터링
    game_records = GameRecord.objects.filter(user=user_id)

    # 직렬화
    serializer = GameRecordSerializer(game_records, many=True)

    return Response({"game_records": serializer.data},status=status.HTTP_200_OK)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def initial_question(request):
    if request.method == "POST":
        """
        초기 질문 생성하는 API
        """
        serializer = InitialQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_list_create(request, movie_id):

    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == "GET":
        comments = Comment.objects.filter(movie=movie)
        serializer = CommentSerializer(comments, many=True)
        print("디버깅 ", serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
