from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv
from django.utils import timezone
from .models import GameRecord, Movie
import json
from rest_framework.response import Response

# .env 파일 로드
load_dotenv()
# API 키 가져오기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 세계관 context 가져오는 함수
def get_movie_context(movie_id):
    # movie = Movie.objects.get(id=movie_id)
    movie = Movie.objects.get(id=movie_id)
    return movie.context


# OpenAI 모델 초기화
chat = ChatOpenAI(temperature=0.5, openai_api_key=OPENAI_API_KEY)


game_record = []  # 각 라운드의 기록

# 프롬프트 템플릿 정의
# 프롬프트를 잘 만지자. 답변 형식도 지정해줘야 할 듯.
evaluation_prompt = PromptTemplate(
    input_variables=["situation", "user_action", "context"],
    template=(
        "상황: {situation}\n"
        "세계관 정보: {context}\n"
        "유저의 행동: {user_action}\n\n"

        "## 1. 유효성 검사\n"
        "- 유저의 입력이 아래 조건을 만족하는지 검토하세요:\n"
        "  1) 무작위 문자열, 의미 없는 숫자 나열인 경우 즉시 0점 처리\n"
        "  2) 최소 20자 이상의 완성된 문장으로 구성되어야 함\n"
        "  3) 상황과 전혀 관계없는 행동은 즉시 0점 처리\n"
        "  4) 비속어나 부적절한 표현이 포함된 경우 즉시 0점 처리\n\n"

        "## 2. 평가 및 응답 형식\n"
        "유저의 행동을 평가하고, 아래 형식에 맞춰 세 줄로 응답하세요:\n"
        "1. 점수: <숫자> (True/False)\n"
        "   점수 기준:\n"
        "   - 0~30점: 매우 비현실적이며 문제 해결에 전혀 기여하지 않습니다.\n"
        "   - 31~50점: 최소한의 논리적 근거는 있지만, 효과적이지 않거나 세계관에 부적합함.\n"
        "   - 51~70점: 세계관에 적합하며 문제 해결에 기여할 가능성이 있지만, 일부 비현실적이거나 부족한 면이 있음.\n"
        "   - 71~100점: 현실적이고 세계관 및 캐릭터 설정에 부합하며 창의적이고 효과적인 행동.\n"
        "2. 이유: 유저의 행동이 캐릭터의 동기와 세계관에 부합하는지, 그리고 서사적으로 긴장감을 높였는지 간결하게 설명하세요.\n"
        "3. 새로운 문제 상황: 유저의 행동을 중심으로 새로운 문제 상황을 작성하세요. 만약 유저의 행동이 유효하지 않은 경우에도, 세계관 정보(context)를 기반으로 새로운 문제 상황을 구성하세요. 문제 상황은 항상 3가지 선택지를 포함하며, 각 선택지는 서로 다른 방향성을 가져야 합니다.\n\n"

        "## 주의사항\n"
        "- 모든 응답은 반드시 아래 형식을 따르며, 추가 텍스트를 포함하지 마세요:\n"
        "1. 점수: <숫자> (True/False)\n"
        "2. 이유: <간결한 이유>\n"
        "3. 새로운 문제 상황: <새로운 문제 상황과 3가지 선택지>\n"
        "- 유효하지 않은 입력이라도 새로운 문제 상황은 반드시 제공되어야 하며, 세계관(context)을 기반으로 생성합니다.\n"
        "- 마지막 라운드(5번째)는 이야기의 결말로 서사적 긴장을 해소하세요.\n"

        "## 예시 응답\n"
        "### 예시 1: 낮은 점수\n"
        "1. 점수: 0 (False)\n"
        "2. 이유: 유저의 행동은 상황과 전혀 무관하며, 비현실적이고 의미 없는 입력입니다.\n"
        "3. 새로운 문제 상황: 나는 적의 비밀 기지에 잠입한 상태다. 그러나 적의 보안 시스템이 강화되었다. 이제 나는 1) 보안 시스템을 해킹해 내부에 접근한다, 2) 팀원과 협력해 새로운 진입 경로를 찾는다, 3) 보안을 무력화하기 위한 장비를 수집한다.\n\n"

        "### 예시 2: 높은 점수\n"
        "1. 점수: 85 (True)\n"
        "2. 이유: 유저의 행동은 긴급 상황에서 현실적이고 창의적인 해결책을 제시했습니다.\n"
        "3. 새로운 문제 상황: 나는 적의 통신망을 차단하려는 임무를 맡았다. 이제 나는 1) 통신 타워를 해킹해 적의 계획을 방해한다, 2) 팀원들과 협력해 적의 통신망을 역추적한다, 3) 적의 본부를 급습해 통신 장비를 직접 파괴한다.\n\n"

        "### 예시 3: 로맨스 시나리오\n"
        "1. 점수: 90 (True)\n"
        "2. 이유: 유저의 행동은 상대방의 감정을 이해하고, 갈등을 해결하려는 성숙한 접근 방식입니다.\n"
        "3. 새로운 문제 상황: 나는 오해로 인해 멀어진 연인과 재회를 준비하고 있다. 이제 나는 1) 진심 어린 편지를 작성해 전달한다, 2) 친구의 도움을 받아 대화를 주선한다, 3) 중요한 이벤트에서 직접 사과하고 화해를 시도한다.\n"
    ),
)




# 게임 진행 요약을 위한 프롬프트
summary_prompt = PromptTemplate(
    input_variables=["history"],
    template=(
        "다음은 유저와의 대화 기록입니다:\n"
        "{history}\n\n"
        "이 기록을 기반으로 전체 이야기를 요약하세요. 요약은 한 편의 영화 줄거리처럼 작성되어야 하며, "
        "유저가 해결한 문제와 그 행동, 그리고 상황의 흐름을 포함해야 합니다. "
    ),
)

# 영화 추천을 위한 프롬프트
eval_prompt = PromptTemplate(
    input_variables=["round1", "round2", "round3", "round4", "round5"],
    template=(
        "다음은 게임의 라운드 데이터입니다:\n"
        "Round 1: {round1}\n"
        "Round 2: {round2}\n"
        "Round 3: {round3}\n"
        "Round 4: {round4}\n"
        "Round 5: {round5}\n\n"
        "이 기록을 기반으로 아래 작업을 수행하세요:\n"
        "1. 이야기 요약: 전체 이야기를 한 편의 영화 줄거리처럼 요약하세요. "
        "요약에는 유저가 해결한 문제, 그 행동, 그리고 상황의 흐름을 포함하세요.\n"
        "2. 심리 분석: 대화 내용을 바탕으로 유저의 감정을 평가하고 심리 상태와 무의식을 추론하세요. "
        "유저의 무의식적인 욕구와 심리적 니즈를 파악하려 노력하세요.\n"
        "3. 영화 추천: 심리 분석 결과를 바탕으로 유저의 감정과 무의식을 반영한 영화를 추천하세요. "
        "추천 영화는 유저의 심리적 상태를 이해하거나 위로할 수 있는 작품이어야 합니다. "
        "단, 추천 영화는 반드시 TMDB 데이터베이스에 등록된 영화여야 합니다.\n\n"
        "참고:\n"
        "- 추천 영화의 이름은 TMDB에서 검색할 수 있도록 정확히 작성하세요.\n"
        "- 추천 영화는 게임 데이터의 기존 영화와는 다른 영화여야 합니다.\n"
        "- TMDB에 등록되지 않은 영화를 추천하지 마세요.\n\n"
        "형식은 다음과 같아야 합니다:\n"
        "1. 이야기 요약: <한 편의 영화처럼 작성된 줄거리>\n"
        "2. 심리 분석: <유저의 감정, 무의식적 욕구, 심리적 상태에 대한 평가>\n"
        "3. 추천 영화:\n"
        "   - 제목: <추천 영화 제목 (TMDB 데이터베이스 등록 이름)>\n"
        "   - 테마: <영화의 주요 테마>\n"
        "   - 추천 이유: <유저의 심리적 상태와의 연관성 및 영화가 제공할 심리적 만족>\n"
    ),
)


# 분석 및 추천 결과 파싱하는 함수.
def analyze_parsing(response_text, game_id):
    """
    AI의 응답 텍스트를 분석하여 각 항목을 분리 및 반환하는 함수.
    """
    try:
        # 텍스트를 줄 단위로 분리
        lines = response_text.split("\n")

        # 각 항목을 초기화
        story_summary = ""
        psychological_analysis = ""
        recommended_movie = {}

        # 현재 읽고 있는 섹션
        current_section = None

        for line in lines:
            line = line.strip()  # 공백 제거

            if line.startswith("1. 이야기 요약:"):
                current_section = "summary"
                story_summary = line.replace("1. 이야기 요약:", "").strip()
            elif line.startswith("2. 심리 분석:"):
                current_section = "psychology"
                psychological_analysis = line.replace("2. 심리 분석:", "").strip()
            elif line.startswith("3. 추천 영화:"):
                current_section = "recommendation"
                current_section = "recommendation"
            elif current_section == "recommendation":
                # 추천 영화 정보 파싱
                if line.startswith("- 제목:"):
                    recommended_movie["title"] = line.replace("- 제목:", "").strip()
                elif line.startswith("- 테마:"):
                    recommended_movie["theme"] = line.replace("- 테마:", "").strip()
                elif line.startswith("- 추천 이유:"):
                    recommended_movie["reason"] = line.replace(
                        "- 추천 이유:", ""
                    ).strip()
            else:
                # 해당 섹션에 내용 추가
                if current_section == "summary":
                    story_summary += f" {line}"
                elif current_section == "psychology":
                    psychological_analysis += f" {line}"

        # 파싱한 뒤에 DB에 추가하기
        game_record = GameRecord.objects.get(id=game_id)

        game_record.total_summary = story_summary
        game_record.emotion = psychological_analysis
        game_record.recommend_movie = recommended_movie["title"]
        game_record.recommend_movie_reason = recommended_movie["reason"]
        game_record.recommend_movie_theme = recommended_movie["theme"]

        game_record.save()

        # 결과 반환
        return {
            "story_summary": story_summary.strip(),
            "psychological_analysis": psychological_analysis.strip(),
            "recommended_movie": recommended_movie,
        }

    except Exception as e:
        print(f"Error parsing response: {e}")
        return None


# 스토리 요약/심리 분석/영화추천 - 결과 분석 
def anlayze_result(round1, round2, round3, round4, round5, game_id):

    llm_chain = LLMChain(llm=chat, prompt=eval_prompt)
    result = llm_chain.run(
        {
            "round1": round1, # 라운드별 데이터 history 데이터 1~5 들어옴.
            "round2": round2,
            "round3": round3,
            "round4": round4,
            "round5": round5,
        }
    )
    # 파싱 고고
    result1 = analyze_parsing(result, game_id)
    return result1


# 행동 평가 및 다음 상황 생성 함수
def evaluate_and_generate_next(situation, user_action, context):
    """
    사용자 행동을 평가하고 다음 상황을 생성하는 함수
    situation, user_action, context 토대로..
    """
    llm_chain = LLMChain(llm=chat, prompt=evaluation_prompt)
    result = llm_chain.run(
        {
            "situation": situation,
            "user_action": user_action,
            "context": context,
        }
    )
    print(result)
    return result


# 평가 결과 처리
def process_evaluation_and_next(result):
    """
    AI의 응답을 분석하여 점수, 유효성, 이유, 다음 문제를 추출하는 함수

    프롬프트를 작성으로 아래와 같은 양식으로 반한된 result.
    줄바꿈을 기준으로 line별로 변수에 할당하고 파싱 진행. 

    양식
    "1. 점수: 90 (True)\n"
    "2. 이유: 유저의 행동은 상대방의 감정을 이해하고, 갈등을 해결 ... \n"
    "3. 새로운 문제 상황: 나는 오해로 인해 멀어진 ...

    """
    # Parsing
    lines = result.split("\n") # 줄바꿈 기준으로 line 나눠줌. 
    try:
        # 점수를 포함한 텍스트에서 숫자만 추출
        score_text = lines[0].split(":")[1].split("(")[0].strip() # 점수 값 찾고
        score = int(score_text)         # 정수로 변환
        is_valid = score >= 50          # 점수에 따라 적절함 판단
    except (ValueError, IndexError):
        score = 0  # 오류 발생 시 기본값 설정

    is_valid = "True" in lines[0]       # 점수에 따라 적절함 판단
    reason = lines[1].replace("2. ", "").strip()    # 이유 
    next_problem = lines[2].replace("3. 새로운 문제 상황: ", "").strip()    # 다음 상황(새로운 상황)

    return score, is_valid, reason, next_problem


# 게임 요약 생성
def generate_summary(history):
    """
    게임 진행 기록을 바탕으로 전체 스토리 요약을 생성하는 함수
    """
    llm_chain = LLMChain(llm=chat, prompt=summary_prompt)
    result = llm_chain.run({"history": history})
    return result

###################################################################
# 게임 진행 메인 로직
def play_game_round(game_record, user_action):
    # history가 문자열일 경우 JSON으로 변환 // history 가져오기.
    if isinstance(game_record.history, str):
        try:
            history = json.loads(game_record.history) or []
        except json.JSONDecodeError:
            history = []
    else:
        history = game_record.history or []

    # 현재 라운드 확인
    current_round = len(history) + 1

    # history에서 현재 상황 가져오기
    if history:
        current_situation = history[-1]["next_situation"]
    else:
        # 기록이 없다면 - 초기 질문 가져오기
        initial_question = game_record.movie.initial_questions.order_by("?").first()
        # 초기 질문이 없다면???
        if not initial_question:
            return Response(
                {"error": "No initial questions available for this movie."}, status=400
            )
        current_situation = initial_question.question

    # 행동 평가 및 다음 상황 생성
    '''
        현재 상황, 유저 입력(시나리오), 세계관 입력
    '''
    evaluation_result = evaluate_and_generate_next(
        situation=current_situation,
        user_action=user_action,
        context=get_movie_context(game_record.movie.id), # 세계관은 즉시 가져오기.
    )

    # 응답 처리 
    '''
        점수, 적절함, 이유, 다음 상황 반환
    '''
    score, is_valid, reason, next_problem = process_evaluation_and_next(evaluation_result)

    # 새로운 라운드 데이터 추가 => history json에 append 될 예정.
    round_data = {
        "round": current_round,             # 현재 라운드
        "situation": current_situation,     # 현재 상황
        "user_action": user_action,         # 유저 입력(시나리오)
        "score": score,                     # 점수 (AI가 판단한 적합성 0~100)
        "evaluation": "적절함" if is_valid else "부적절함", # 점수에 따른 적절함
        "reason": reason,                   # 점수에 대한 이유
        "next_situation": next_problem,     # 다음 상황 (= 입력*현재상황)
    }
    print(round_data)

    # 중복 방지: 현재 라운드가 이미 존재하는지 확인
    if not any(entry["round"] == current_round for entry in history):
        history.append(round_data)

    # 기록 업데이트
    game_record.history = json.dumps(history, ensure_ascii=False)  # 직렬화하여 JSON으로 저장
    game_record.total_score += score

    # 게임 종료 조건 확인
    is_game_over = len(history) >= 5
    if is_game_over:
        game_record.end_time = timezone.now()
        game_record.end_status = "COMPLETED"

    game_record.save()
    print("game_record 저장")

    return next_problem, is_game_over, reason, is_valid

# 게임 요약 함수
def generate_game_summary(game_record):
    history = (
        json.loads(game_record.history)
        if isinstance(game_record.history, str)
        else game_record.history
    )

    formatted_history = "\n".join(
        f"라운드 {entry.get('round', 'N/A')}: [상황]: {entry.get('situation', 'N/A')}\n"
        f" [행동]: {entry.get('user_action', 'N/A')}\n"
        f" [평가]: {entry.get('evaluation', 'N/A')}, 점수: {entry.get('score', 0)}"
        for entry in history
    )

    summary = generate_summary(formatted_history)
    return summary
