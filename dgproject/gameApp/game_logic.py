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

def get_movie_context(movie_id):
    #movie = Movie.objects.get(id=movie_id)
    movie = Movie.objects.get(id=movie_id)
    return movie.context


# OpenAI 모델 초기화
chat = ChatOpenAI(temperature=0.5, openai_api_key=OPENAI_API_KEY)


game_record = [  # 각 라운드의 기록
    
]

# 프롬프트 템플릿 정의
# 프롬프트를 잘 만지자. 답변 형식도 지정해줘야 할 듯.
evaluation_prompt = PromptTemplate(
    input_variables=["situation", "user_action", "context"],
    template = (
        "상황: {situation}\n"
        "세계관 정보: {context}\n"
        "유저의 행동: {user_action}\n\n"
        "아래의 형식에 맞춰 응답하세요:\n"
        "1. 점수: <숫자> (True/False)\n"
        "   점수 기준:\n"
        "   - 0~30점: 유저의 행동이 매우 비현실적이며, 세계관과 캐릭터 설정에 어긋나고, 문제 해결에 전혀 기여하지 않습니다. 예: 의미 없는 무작위 문자열(예: `ㅁㄴㅇㅎㅂㅈ더ㅠㅣㅏㅓ5123`)을 입력하거나, 상황과 전혀 관련 없는 비논리적인 행동을 선택함.\n"
        "   - 31~50점: 행동이 세계관에 적합하지 않거나 효과적이지 않더라도, 최소한의 논리적 근거는 있습니다. 예: 적과 협상을 시도하지만 설득력이 부족하거나, 문제 상황에서 상황과 관련 없는 자원을 사용하는 행동.\n"
        "   - 51~70점: 행동이 세계관에 적합하더라도 문제 해결에 기여할 가능성이 있지만, 일부 비현실적이거나 전략적으로 부족한 면이 있습니다. 예: 적의 기지를 폭파하려 하나 정확한 정보를 모른 채 행동함.\n"
        "   - 71~100점: 행동이 매우 현실적이고 세계관 및 캐릭터 설정에 부합하지 않더라도 창의적으로, 문제 해결에 효과적으로 기여합니다. 예: 제한된 자원으로 창의적이고 설득력 있는 계획을 세워 적을 물리침.\n"
        "   - 추가 점수: 유저가 작성한 시나리오에서 이유가 구체적이고 합당할 경우 세계관과 벗어나더라도 추가점수를 부여합니다."
        "   - 주의: 단 총점수는 100점을 넘지 않습니다."
        "2. 이유: <한 문단으로 간결하게 작성하며, 영화 시나리오 전문가의 시각에서 다음을 평가하세요: 1) 유저의 행동이 캐릭터의 내적 동기와 세계관 설정에 부합하는지, 2) 이 행동이 이야기의 서사적 전개 및 긴장감 형성에 어떻게 기여하거나 방해하는지.>\n"
        "3. 새로운 문제 상황: <한 문단으로 작성하며, 다음 요소를 포함하세요: 현재 상황의 여파, 새롭게 발생한 긴장 요소, 캐릭터가 극복해야 할 구체적인 목표. 그리고 유저가 취할 수 있는 두 가지 이상의 구체적인 행동 방향을 명시하세요. 각 행동은 서로 다른 결과를 유도할 수 있는 선택지여야 합니다. 예: '적의 기습으로 동료가 포로로 잡혔으며, 유저는 제한된 시간 안에 정보를 얻고 동료를 구출해야 합니다. 유저의 선택: 1) 적의 기지로 잠입하여 은밀히 동료를 구출하려 한다. 2) 적과의 협상을 시도해 동료를 안전히 되찾으려 한다. 3) 동료의 구출을 포기하고 적의 주요 거점을 공격해 전략적 우위를 점하려 한다.'>"
        "주의: 각 항목은 줄바꿈 없이 한 줄로 작성하며, 번호로 시작해야 합니다. \n"
        "주의2: 새로운 문제 상황은 상황에 따른 유저의 행동으로 발생할 상황에 대해 자세하게 적어야 합니다.\n"
        "참고: 응답은 영화 시나리오 작성자의 관점에서, 사건의 서사적 전개와 캐릭터 간의 갈등 및 협력 요소를 강화하도록 작성하세요. 또한 영화 기존의 시나리오에서 크게 벗어나도 괜찮습니다.\n"
        "참고2: 5번째 라운드는 마지막 라운드로 5번째 새로운 문제상황은 결말을 지어주세요."        
        "참고3: 5번째 라운드 결말의 비극 희극 여부는 유저의 점수를 기준으로 판단하여 작성해주세요"
        "예시 응답 1:\n"
        "1. 점수: 20 (False)\n"
        "2. 이유: 유저의 행동은 세계관의 설정과 캐릭터의 동기에서 완전히 벗어나 있으며, 서사적 긴장감을 훼손하는 매우 비현실적인 선택입니다. 이는 이야기의 흐름을 방해하고 문제 해결에 전혀 기여하지 않습니다.\n"
        "3. 새로운 문제 상황: 주인공이 적의 비밀 연구소를 탈출한 직후, 적이 도시에 바이러스를 퍼뜨리기 위해 움직인다는 정보를 얻습니다. 유저는 두 가지 선택에 직면합니다. 적의 계획을 막기 위해 시간 제한 내에 연구소의 서버를 해킹해 정보를 수집하거나, 도시에 도달하기 전에 적의 주요 병력을 정면으로 공격해 시간을 벌고 시민들을 대피시킨다. 각 선택은 성공 가능성과 위험 요소가 다르며, 캐릭터의 결단력을 시험합니다.\n"
        "예시 응답 2.\n"
        "1. 점수: 85 (True)"
        "2. 이유: 유저의 행동은 상황의 긴급성을 고려한 현실적이고 전략적인 선택으로, 서사적 긴장감을 높이며 캐릭터의 능력을 창의적으로 활용한 훌륭한 대응입니다. 이는 관객의 몰입도를 유지하며 문제 해결 가능성을 높입니다."
        "3. 새로운 문제 상황: 적의 함정에서 가까스로 탈출한 유저는 적이 도주 중에 도시의 주요 통신망을 장악하려 한다는 정보를 얻습니다. 유저는 두 가지 선택에 직면하여 두가지 기로에 섭니다. 적이 통신망에 접근하기 전에 주변 경찰과 협력해 방어선을 구축하거나 적의 행동을 방해하기 위해 통신망 접근 지점에 미리 잠입해 시간을 벌며, 추가적인 증거를 확보하려 한다."
        "예시 응답 3.\n"
        "1. 점수: 80 (True)"
        "2. 이유: 유저의 행동은 캐릭터의 감정적 동기를 이해하고, 상대방과의 갈등을 해결하려는 성숙한 접근 방식을 보여줍니다. 이는 서사적으로도 관계의 발전을 돕고 관객의 공감을 불러일으키는 선택입니다."
        "3. 새로운 문제 상황: 주인공은 사랑하는 사람이 큰 오해로 인해 멀어지려는 순간, 상대방이 중요한 발표를 앞두고 극도로 불안해하고 있다는 사실을 알게 됩니다. 유저는 두 가지 선택지가 있을 수 있습니다. 상대방의 오해를 풀기 위해 직접 진심을 담은 편지를 쓰고 발표 직전에 전달하거나 발표장에서 상대방을 조용히 응원하며 발표가 끝난 뒤 오해를 풀기 위한 대화를 시도한다."

))

# 게임 진행 요약을 위한 프롬프트
summary_prompt = PromptTemplate(
    input_variables = ["history"],
    template = (
        "다음은 유저와의 대화 기록입니다:\n"
        "{history}\n\n"
        "이 기록을 기반으로 전체 이야기를 요약하세요. 요약은 한 편의 영화 줄거리처럼 작성되어야 하며, "
        "유저가 해결한 문제와 그 행동, 그리고 상황의 흐름을 포함해야 합니다. "
    )
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
        "2. 심리 분석: 대화 내용을 바탕으로 유저의 감정을 평가하고 심리 상태를 추론하세요. "
        "유저의 무의식적인 욕구와 심리적 니즈를 파악하려 노력하세요.\n"
        "3. 영화 추천: 심리 분석 결과를 바탕으로 유저의 감정과 무의식을 반영한 영화를 추천하세요. "
        "추천 영화는 유저의 심리적 상태를 이해하거나 위로할 수 있는 작품이어야 합니다.\n\n"
        "참고 : 추천 영화의 이름은 TMDB에서 검색에 활용할 수 있도록 작성해주세요."
        "주의 : 위 데이터의 영화와는 다른 영화를 추천하세요."
        "형식은 다음과 같아야 합니다:\n"
        "1. 이야기 요약: <한 편의 영화처럼 작성된 줄거리>\n"
        "2. 심리 분석: <유저의 감정, 무의식적 욕구, 심리적 상태에 대한 평가>\n"
        "3. 추천 영화:\n"
        "   - 제목: <추천 영화 제목>\n"
        "   - 테마: <영화의 주요 테마>\n"
        "   - 추천 이유: <유저의 심리적 상태와의 연관성 및 영화가 제공할 심리적 만족>\n"
        
    )
)

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
                    recommended_movie["reason"] = line.replace("- 추천 이유:", "").strip()
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
        game_record.recommend_movie = recommended_movie['title']
        game_record.recommend_movie_reason = recommended_movie['reason']
        game_record.recommend_movie_theme = recommended_movie['theme']

        game_record.save()


        # 결과 반환
        return {
            "story_summary": story_summary.strip(),
            "psychological_analysis": psychological_analysis.strip(),
            "recommended_movie": recommended_movie
        }
    
    except Exception as e:
        print(f"Error parsing response: {e}")
        return None

# 5라운드에 대한 결과 분석
def anlayze_result(round1, round2,round3,round4,round5, game_id):
    
    llm_chain = LLMChain(llm=chat, prompt=eval_prompt)
    result = llm_chain.run({
        "round1": round1,
        "round2": round2,
        "round3": round3,
        "round4": round4,
        "round5": round5,
    })
    print(result)
    result1 = analyze_parsing(result, game_id)
    print(result1)
    return result1


# 행동 평가 및 다음 상황 생성 함수
def evaluate_and_generate_next(situation, user_action,context):
    """
    사용자 행동을 평가하고 다음 상황을 생성하는 함수
    """
    llm_chain = LLMChain(llm=chat, prompt=evaluation_prompt)
    result = llm_chain.run({
        "situation": situation,
        "user_action": user_action,
        "context" : context,
    })
    print(result)
    return result

# 평가 결과 처리
def process_evaluation_and_next(result):
    """
    AI의 응답을 분석하여 점수, 유효성, 이유, 다음 문제를 추출하는 함수
    """
    lines = result.split("\n")
    try:
        # 점수를 포함한 텍스트에서 숫자만 추출
        score_text = lines[0].split("점")[0].split()[-1].strip()
        score = int(score_text)  # 정수로 변환
        is_valid = score >=50
    except (ValueError, IndexError):
        score = 0  # 오류 발생 시 기본값 설정
    
    is_valid = "True" in lines[0]
    reason = lines[1].replace("2. ", "").strip()
    next_problem = lines[2].replace("3. 새로운 문제 상황: ", "").strip()
    
    return score, is_valid, reason, next_problem


# 게임 요약 생성
def generate_summary(history):
    """
    게임 진행 기록을 바탕으로 전체 스토리 요약을 생성하는 함수
    """
    llm_chain = LLMChain(llm=chat, prompt=summary_prompt)
    result = llm_chain.run({
        "history":history
    })
    return result



def play_game_round(game_record, user_action):
    # history가 문자열일 경우 JSON으로 변환
    if isinstance(game_record.history, str):
        try:
            history = json.loads(game_record.history) or []
        except json.JSONDecodeError:
            history = []
    else:
        history = game_record.history or []

    # 현재 라운드 확인
    current_round = len(history) + 1

    # 현재 상황 가져오기
    if history:
        current_situation = history[-1]['next_situation']
    else:
        # 초기 질문 설정
        initial_question = game_record.movie.initial_questions.order_by('?').first()
        if not initial_question:
            return Response({"error": "No initial questions available for this movie."}, status=400)
        current_situation = initial_question.question

    # 행동 평가 및 다음 상황 생성
    evaluation_result = evaluate_and_generate_next(
        situation=current_situation,
        user_action=user_action,
        context=get_movie_context(game_record.movie.id),
    )
    

    # 응답 처리
    score, is_valid, reason, next_problem = process_evaluation_and_next(evaluation_result)

    # 새로운 라운드 데이터 추가
    round_data = {
        "round": current_round,
        "situation": current_situation,
        "user_action": user_action,
        "score": score,
        "evaluation": "적절함" if is_valid else "부적절함",
        "reason": reason,
        "next_situation": next_problem
    }

    # 중복 방지: 현재 라운드가 이미 존재하는지 확인
    if not any(entry['round'] == current_round for entry in history):
        history.append(round_data)

    # 기록 업데이트
    game_record.history = json.dumps(history, ensure_ascii=False)  # 직렬화하여 JSON으로 저장
    game_record.total_score += score

    # 게임 종료 조건 확인
    is_game_over = len(history) >= 5
    if is_game_over:
        game_record.end_time = timezone.now()
        game_record.end_status = 'COMPLETED'

    game_record.save()
    print('game_record 저장')

    return next_problem, is_game_over, reason, is_valid

def play_game_round2(game_record, user_action):
    # history 초기화
    if isinstance(game_record.history, str):
        try:
            history = json.loads(game_record.history) or []
        except json.JSONDecodeError:
            history = []
    else:
        history = game_record.history or []

    # 현재 라운드 계산
    # current_round = len(history) + 1
    if not history:
        current_round = 0  # 첫 라운드일 경우 0으로 설정
    else :
        current_round +=1

    # 현재 상황 가져오기
    if history:
        current_situation = history[-1]['next_situation']
    else:
        # 초기 질문 설정
        initial_question = game_record.movie.initial_questions.order_by('?').first()
        if not initial_question:
            return Response({"error": "No initial questions available for this movie."}, status=400)

        # 첫 라운드 생성
        current_situation = initial_question.question
        round_data = {
            "round": 1,
            "situation": current_situation,
            "user_action": None,
            "score": 0,
            "evaluation": None,
            "reason": None,
            "next_situation": None
        }
        history.append(round_data)

    # 행동 평가 및 다음 상황 생성
    evaluation_result = evaluate_and_generate_next(
        situation=current_situation,
        user_action=user_action,
        context=get_movie_context(game_record.movie.id),
    )

    # 응답 처리
    score, is_valid, reason, next_problem = process_evaluation_and_next(evaluation_result)

    # 라운드 데이터 생성
    round_data = {
        "round": current_round,
        "situation": current_situation,
        "user_action": user_action,
        "score": score,
        "evaluation": "적절함" if is_valid else "부적절함",
        "reason": reason,
        "next_situation": next_problem
    }

    # 중복 방지 및 추가
    if history and any(entry['round'] == current_round for entry in history):
        print(f"Round {current_round} already exists in history.")
    else:
        history.append(round_data)

    # 기록 업데이트
    game_record.history = json.dumps(history, ensure_ascii=False)
    game_record.total_score += score

    # 게임 종료 조건 확인
    is_game_over = len(history) >= 5
    if is_game_over:
        game_record.end_time = timezone.now()
        game_record.end_status = 'COMPLETED'

    game_record.save()

    # 디버깅 로그 추가
    print(f"Current Round: {current_round}")
    print(f"History Length: {len(history)}")
    print(f"History Data: {history}")
    print(f"Next Problem: {next_problem}")
    print(f"Is Game Over: {is_game_over}")

    return next_problem, is_game_over, reason, is_valid

    # history 초기화
    if isinstance(game_record.history, str):
        try:
            history = json.loads(game_record.history) or []
        except json.JSONDecodeError:
            history = []
    else:
        history = game_record.history or []

    # 현재 라운드 계산
    current_round = len(history) + 1

    # 현재 상황 가져오기
    if history:
        current_situation = history[-1]['next_situation']
    else:
        # 초기 질문 설정
        initial_question = game_record.movie.initial_questions.order_by('?').first()
        if not initial_question:
            return Response({"error": "No initial questions available for this movie."}, status=400)

        # 첫 라운드 생성
        current_situation = initial_question.question
        first_round_data = {
            "round": current_round,
            "situation": current_situation,
            "user_action": None,
            "score": 0,
            "evaluation": None,
            "reason": None,
            "next_situation": None
        }
        history.append(first_round_data)

    # 행동 평가 및 다음 상황 생성
    evaluation_result = evaluate_and_generate_next(
        situation=current_situation,
        user_action=user_action,
        context=get_movie_context(game_record.movie.id),
    )

    # 응답 처리

def play_game_round4(game_record, user_action):
    # history 초기화
    if isinstance(game_record.history, str):
        try:
            history = json.loads(game_record.history) or []
        except json.JSONDecodeError:
            history = []
    else:
        history = game_record.history or []

    # 현재 라운드 계산
    current_round = len(history) + 1

    # 현재 상황 가져오기
    if history:
        current_situation = history[-1]['next_situation']
    else:
        # 초기 질문 설정
        initial_question = game_record.movie.initial_questions.order_by('?').first()
        if not initial_question:
            return None, None, "No initial questions available for this movie.", False  # 기본 반환값
        # 첫 라운드 데이터 추가
        current_situation = initial_question.question
        first_round_data = {
            "round": current_round,
            "situation": current_situation,
            "user_action": None,
            "score": 0,
            "evaluation": None,
            "reason": None,
            "next_situation": None
        }
        history.append(first_round_data)

    # 행동 평가 및 다음 상황 생성
    try:
        evaluation_result = evaluate_and_generate_next(
            situation=current_situation,
            user_action=user_action,
            context=get_movie_context(game_record.movie.id),
        )
        
        # 응답 처리
        score, is_valid, reason, next_problem = process_evaluation_and_next(evaluation_result)
    except Exception as e:
        return None, None, str(e), False  # 예외 발생 시 기본 반환값

    # 새로운 라운드 데이터 추가
    round_data = {
        "round": current_round,
        "situation": current_situation,
        "user_action": user_action,
        "score": score,
        "evaluation": "적절함" if is_valid else "부적절함",
        "reason": reason,
        "next_situation": next_problem
    }
    history.append(round_data)

    # 기록 업데이트
    game_record.history = json.dumps(history, ensure_ascii=False)
    game_record.total_score += score

    # 게임 종료 조건 확인
    is_game_over = len(history) >= 5
    if is_game_over:
        game_record.end_time = timezone.now()
        game_record.end_status = 'COMPLETED'

    game_record.save()

    # 디버깅 로그 추가
    print(f"Current Round: {current_round}")
    print(f"History Length: {len(history)}")
    print(f"History Data: {history}")
    print(f"Next Problem: {next_problem}")
    print(f"Is Game Over: {is_game_over}")

    # 모든 조건에서 반환
    return next_problem, is_game_over, reason, is_valid

def generate_game_summary(game_record):
    history = json.loads(game_record.history) if isinstance(game_record.history, str) else game_record.history
    
    formatted_history = "\n".join(
        f"라운드 {entry.get('round', 'N/A')}: [상황]: {entry.get('situation', 'N/A')}\n"
        f" [행동]: {entry.get('user_action', 'N/A')}\n"
        f" [평가]: {entry.get('evaluation', 'N/A')}, 점수: {entry.get('score', 0)}"
        for entry in history
    )
    
    summary = generate_summary(formatted_history)
    return summary