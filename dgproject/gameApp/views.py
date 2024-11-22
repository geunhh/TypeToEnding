from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.response import Response
from .models import GameRecord, Movie
from .game_logic import play_game_round, generate_game_summary, anlayze_result
from .serializers import MovieSerializer, GameRecordSerializer
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import pprint
import json


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def movielist(request):
    """
    전체 영화 목록을 반환하는 API

    Returns:
        Response: 직렬화된 영화 데이터 목록
    """
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


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
        return Response({"error": "Movie not found"}, status=404)

    # User = get_user_model()         # 유저모델에서
    user = user = request.user

    initial_question = movie.initial_questions.order_by("?").first()

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

    if not initial_question:
        return Response(
            {"error": "No initial questions available for this movie."}, status=400
        )
    print(game_record)
    return Response(
        {
            "game_id": game_record.id,
            "initial_question": initial_question.question,
        }
    )


@api_view(["POST"])
def play_game(request, game_id):
    """
    게임 진행을 처리하는 API

    Args:
        request: 사용자 행동이 포함된 요청 객체
        game_id: 진행할 게임의 ID

    Returns:
        Response: 다음 문제, 게임 종료 여부, 총점, 평가 이유, 유효성 여부
    """
    game_record = GameRecord.objects.get(
        id=game_id
    )  # 기존에 진행했던 게임 데이터 찾음.

    user_action = request.data.get("user_action")  # user_acton. 작성한 시나리오 가져옴.

    # 게임 record와 작성한 시나리오 던지기
    next_problem, is_game_over, reason, is_valid = play_game_round(
        game_record, user_action
    )

    response_data = {
        "next_problem": next_problem,
        "is_game_over": is_game_over,
        "total_score": game_record.total_score,
        "reason": reason,
        "is_valid": is_valid,
    }

    if is_game_over:
        summary = generate_game_summary(game_record)
        response_data["summary"] = summary

    return Response(response_data)


@api_view(["GET"])
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
    return Response({"summary": summary, "total_score": game_record.total_score})


@api_view(["GET"])
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
    return Response({"history": game_record.history})


@api_view(["POST"])
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

    return Response({"result": result})


@api_view(["GET"])
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

    return Response({"game_records": serializer.data})
