from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv
from django.utils import timezone
from .models import GameRecord, Movie
import json

# .env 파일 로드
load_dotenv()
# API 키 가져오기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def get_movie_context(movie_id):
    #movie = Movie.objects.get(id=movie_id)
    movie = Movie.objects.get(id=1) # 일단 1로..
    return movie.context

## 해리포터 세계관. 정보
harry_potter_context = """
해리포터는 마법 세계를 배경으로 한 이야기로, 마법사, 마녀, 마법 생물, 어둠의 마법사들 간의 갈등과 모험을 그립니다. 주요 내용과 설정은 다음과 같습니다.

1. 주요 등장인물:
- 해리 포터 (Harry Potter): 마법 세계의 영웅으로 여겨지며, '선택된 아이'로 불립니다. 볼드모트의 가장 큰 적으로, 그의 이마에는 번개 모양의 흉터가 있습니다.
- 헤르미온느 그레인저 (Hermione Granger): 해리의 가장 똑똑한 친구로, 마법 이론과 실전에 모두 능합니다. 항상 냉철한 판단을 내립니다.
- 론 위즐리 (Ron Weasley): 해리의 충실한 친구로, 용기 있고 의리를 중시합니다. 가끔 실수를 하지만 중요한 순간에 큰 역할을 합니다.
- 알버스 덤블도어 (Albus Dumbledore): 호그와트의 교장으로, 현명하고 강력한 마법사입니다. 해리에게 중요한 조언과 도움을 줍니다.
- 볼드모트 (Lord Voldemort): 어둠의 군주로 불리며, 순수 혈통을 중시하는 사악한 마법사입니다. 호크룩스라는 어둠의 마법으로 자신의 영혼을 나누어 불사신이 되려 합니다.
- 세베루스 스네이프 (Severus Snape): 포션 교수이자 이중 스파이로, 그의 진정한 충성심은 마지막까지 미스터리로 남습니다.
- 드레이코 말포이 (Draco Malfoy): 순수혈통을 자랑하는 말포이 가문의 아들로, 해리와 항상 대립합니다.
- 루나 러브굿 (Luna Lovegood): 독특하고 창의적인 성격을 가진 해리의 친구로, 마법 세계의 다양한 생물에 대해 깊은 지식을 가지고 있습니다.

2. 주요 장소:
- 호그와트 마법학교 (Hogwarts): 마법사와 마녀들이 교육을 받는 학교로, 네 개의 기숙사(그리핀도르, 슬리데린, 후플푸프, 래번클로)가 있습니다. 성은 여러 가지 마법으로 보호되고 있으며, 비밀 통로와 숨겨진 방이 많습니다.
- 어둠의 숲 (Forbidden Forest): 위험한 마법 생물들이 살고 있는 숲으로, 학내 규칙상 접근이 금지된 장소입니다.
- 다이애건 앨리 (Diagon Alley): 마법사들이 쇼핑을 하는 거리로, 마법 지팡이, 빗자루, 마법책 등을 구매할 수 있습니다.
- 그린고트 은행 (Gringotts): 마법 세계의 유일한 은행으로, 고블린들이 운영하며 매우 강력한 보안을 자랑합니다.
- 아즈카반 (Azkaban): 마법사들이 수감되는 감옥으로, 디멘터라는 어둠의 생물이 경비를 서고 있습니다.

3. 마법과 마법 아이템:
- 마법 지팡이 (Wand): 마법을 사용할 때 필요한 도구로, 각각의 지팡이는 사용자와 독특한 연결을 형성합니다.
- 호크룩스 (Horcrux): 영혼을 나눠 물건에 저장하여 죽음을 피할 수 있는 어둠의 마법입니다.
- 투명 망토 (Invisibility Cloak): 사용자를 투명하게 만들어 숨거나 도망칠 때 유용합니다.
- 죽음의 성물 (Deathly Hallows): 세 가지 강력한 마법 아이템으로, elder wand, resurrection stone, invisibility cloak가 포함됩니다.
- 퀴디치 빗자루 (Quidditch Broomstick): 마법 세계에서 비행할 때 사용하는 도구입니다.

4. 주요 갈등:
- 볼드모트와의 전쟁: 마법 세계를 지배하려는 볼드모트와 그를 막으려는 저항 세력(덤블도어의 군대, 피닉스 기사단) 간의 대립.
- 혈통 문제: 순수 혈통 마법사와 머글 태생 마법사(머글 부모에게서 태어난 마법사) 간의 차별과 갈등.
- 호그와트의 비밀: 비밀의 방, 죽음의 성물, 호그와트 내 숨겨진 통로 등 학교 자체가 다양한 미스터리를 품고 있음.

5. 마법 생물:
- 히포그리프 (Hippogriff): 말과 독수리의 혼합 생물로, 매우 예의를 중시합니다.
- 디멘터 (Dementor): 영혼을 흡수하며, 아즈카반을 경비하는 어둠의 생물.
- 드래곤 (Dragon): 강력하고 위험한 생물로, 불을 뿜으며 금고를 지키는 데 사용되기도 합니다.
- 도비 (Dobby): 집요정으로, 해리에게 중요한 도움을 준 충직한 존재입니다.
- 페닉스 (Phoenix): 불사조로, 재에서 다시 태어나며 치유의 능력을 가지고 있습니다.

이 모든 설정은 해리포터 세계관을 구성하며, 당신은 이 설정에 기반하여 게임 시나리오를 진행하고, 문제를 해결해야 합니다.
"""

# OpenAI 모델 초기화
chat = ChatOpenAI(temperature=0.5)


game_record = [  # 각 라운드의 기록
]

########################################################################
############################ 템플릿 모음 ################################
# 프롬프트 템플릿
evaluation_prompt = PromptTemplate(
    input_variables=["situation", "user_action", "context"],
    template=(
        "상황: {situation}\n"
        "세계관 정보: {context}\n"
        "유저의 행동: {user_action}\n\n"
        "질문:\n"
        "1. 유저의 행동을 0~100 점으로 평가하고, 50점을 기준으로 True 또는 False로 적절성을 판단하세요.\n"
        "2. 판단의 이유를 설명하세요.\n"
        "3. 이 상황에서 이어지는 새로운 문제 상황을 작성하세요. 새로운 문제 상황은 해리포터 세계관에 맞게 작성하고, "
        "유저가 해결해야 할 도전 과제를 포함해야 합니다."
    )
)

summary_prompt = PromptTemplate(
    input_variables = ["history"],
    template = (
        "다음은 유저와의 대화 기록입니다:\n"
        "{history}\n\n"
        "이 기록을 기반으로 전체 이야기를 요약하세요. 요약은 한 편의 영화 줄거리처럼 작성되어야 하며, "
        "유저가 해결한 문제와 그 행동, 그리고 상황의 흐름을 포함해야 합니다. "
    )
)
################################################################
################################################################


# 행동 평가 및 다음 상황 생성 함수
def evaluate_and_generate_next(situation, user_action,context):
    llm_chain = LLMChain(llm=chat, prompt=evaluation_prompt)
    result = llm_chain.run({
        "situation": situation,
        "user_action": user_action,
        "context" : context,
    })
    return result

def process_evaluation_and_next(result):
    # 응답 분석
    lines = result.split("\n")
    try:
        # 점수를 포함한 텍스트에서 숫자만 추출
        score_text = lines[0].split("점")[0].split()[-1].strip()
        score = int(score_text)  # 정수로 변환
    except (ValueError, IndexError):
        score = 0  # 오류 발생 시 기본값 설정
    
    is_valid = "True" in lines[0]
    reason = lines[1].replace("2. ", "").strip()
    next_problem = lines[2].replace("3. 새로운 문제 상황: ", "").strip()
    
    return score, is_valid, reason, next_problem



def generate_summary(history):
    llm_chain = LLMChain(llm=chat, prompt=summary_prompt)
    result = llm_chain.run({
        "history":history
    })
    return result


#####################################################################
############################## 메인 루프 #############################
# def game_loop():
    # 첫 시나리오 설정
    current_situation = {
        "id": 1,
        "movie": "Harry Potter",
        "situation": "당신은 호그와트 도서관에 있습니다. 볼드모트의 추종자들이 당신을 찾고 있습니다. 도망칠 방법을 찾아야 합니다."
    }
    context = harry_potter_context  # 영화 세계관 정보
    game_round = 0  # 게임 회차
    
    history = []  # 게임 진행 기록 저장

    while True:
        print(f"\n🧩 [현재 상황]: {current_situation['situation']}")
        
        # 유저 행동 입력
        user_action = input("🔍 [당신의 대처는?]: ")

        # 행동 평가 및 새로운 문제 상황 생성
        print("\n📝 [결과 평가 중...]\n")
        evaluation_result = evaluate_and_generate_next(
            situation=current_situation["situation"],
            user_action=user_action,
            context=context
        )

        # 응답 처리
        score, is_valid, reason, next_problem = process_evaluation_and_next(evaluation_result)

        # 상세 결과 출력
        print("✅ [평가 결과]")
        print(f"   행동 점수: {score}")
        print(f"   적절성 여부: {'Yes' if is_valid else 'No'}")
        print(f"   이유: {reason}")
        print(f"\n📖 [새로운 문제 상황]: {next_problem}")

        # 히스토리 저장
        history.append({
            'round': game_round + 1,
            'situation': current_situation['situation'],
            'user_action': user_action,
            'eval': "적절함" if is_valid else "부적절함",
            'score': score
        })

        # 종료 조건 확인
        if "게임 종료" in next_problem:
            print("\n💀 [게임 종료!]: 새로운 문제 상황에 '게임 종료' 조건이 포함되었습니다.")
            break
        elif game_round >= 4:  # 최대 5회로 제한
            print("\n🕒 [게임 종료!]: 최대 라운드(5회)를 초과했습니다.")
            break

        # 다음 상황 설정
        game_record.append(
            {
                "round": game_round,
                "situation": current_situation['situation'],
                "user_action": user_action,
                "score": score,
                "evaluation": True if score > 50 else False,
                "reason": reason,
                "next_situation": next_problem
            }
        )


        current_situation = {"situation": next_problem}
        game_round += 1


    ############################################################################
    # 요약 생성 및 출력
    print("\n🎞 [전체 시나리오 요약]")
    formatted_history = "\n".join(
        f"라운드 {entry['round']}: [상황]: {entry['situation']}\n"
        f"   [행동]: {entry['user_action']}\n"
        f"   [평가]: {entry['eval']}, 점수: {entry['score']}"
        for entry in history
    )
    summary = generate_summary(formatted_history)
    print(summary)

    game_record.append({"summary":summary})

def play_game_round(game_record, user_action):
    context = get_movie_context(game_record.movie.id)
    # 이전 라운드 데이터 or 첫 질문 가져오기
    if game_record.history:
        history = json.loads(game_record.history)
        current_situation = history[-1]['next_situation']
    else :
        current_situation = game_record.movie.initial_questions.order_by('?').first().question
    
    evaluation_result = evaluate_and_generate_next(
        situation = current_situation,
        user_action=user_action,
        context = context,
    )
    
    score, is_valid, reason, next_problem = process_evaluation_and_next(evaluation_result)

    round_data = {
        "round": len(history) + 1 if game_record.history else 1,
        "situation": current_situation,
        "user_action": user_action,
        "score": score,
        "evaluation": "채택" if is_valid else "폐기",
        "reason": reason,
        "next_situation": next_problem
    }

    if game_record.history:
        history.append(round_data)
    else:
        history = [round_data]

    game_record.history = json.dumps(history)
    game_record.total_score += score

    is_game_over = len(history) >= 5

    if is_game_over:
        game_record.end_time = timezone.now()
        game_record.end_status = 'COMPLETED'
    
    game_record.save()

    return next_problem, is_game_over

def generate_game_summary(game_record):
    history = json.loads(game_record.history)
    formatted_history = "\n".join(
        f"라운드 {entry['round']}: [상황]: {entry['situation']}\n"
        f"   [행동]: {entry['user_action']}\n"
        f"   [평가]: {entry['evaluation']}, 점수: {entry['score']}"
        for entry in history
    )
    summary = generate_summary(formatted_history)
    return summary
