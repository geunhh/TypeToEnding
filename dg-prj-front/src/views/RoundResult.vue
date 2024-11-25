<template>
    <div class="bigbig-container">
        <div class="playgame-container">
            <!-- <p>{{ moviestore.movie_name }}</p>
        <p>{{ moviestore.description }}</p> -->
            <!-- 상단 bar -->
            <div class="high-bar">
                <div class="bar-content">
                    <!-- 라운드 표시 -->
                    <div class="round-section">
                        <div class="round-circle">
                            <span class="round-label">ROUND</span>
                            <span class="round-number">{{ gamestore.game_round + 1 }}</span>
                        </div>
                    </div>

                    <!-- 영화/감독 정보 -->
                    <div class="info-section">
                        <div class="info-row">
                            <i class="bi bi-film"></i>
                            <span class="info-label">영화</span>
                            <span class="info-value">{{ moviestore.movie_name }}</span>
                        </div>
                        <div class="info-row">
                            <i class="bi bi-person-badge"></i>
                            <span class="info-label">감독</span>
                            <span class="info-value">{{ accountstore.userInfo.name }}</span>
                        </div>
                    </div>

                    <!-- 진행 상황 -->
                    <div class="progress-section">
                        <div class="date-display">
                            <i class="bi bi-calendar3"></i>
                            <span>{{ year }} / {{ month }} / {{ day }}</span>
                        </div>
                        <div class="progress-indicators">
                            <div v-for="n in 5" :key="n" class="progress-dot"
                                :class="{ 'active': gamestore.game_round >= n - 1 }">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- 시나리오를 채택/폐기합니다. -->
            <div class="description-box">
                <span class="scenario-result">
                    시나리오를
                </span>
                <span class="selected" v-if="result.is_valid">
                    채택
                </span>
                <span class="discarded" v-else>
                    폐기
                </span>
                <span class="scenario-result">
                    합니다
                </span>
            </div>

            <!-- 유저가 작성한 시나리오 및 평가 결과-->
            <div class="scenario-container">
                <div class="scenario-box">
                    <p>{{ gamestore.user_action1 }}</p>
                    <!-- {{ gamestore.user_action1 }} -->
                </div>

                <div class="prompt-box">
                    <p>{{ result.reason }}</p>
                </div>

            </div>
            <div class="d-flex justify-content-center">
                <button type="button" class="btn btn-danger" @click="nextStage" style="margin-top: 15px;">
                    <span v-if="gamestore.game_round == 4">결말보기</span>
                    <span v-else>다음으로</span>
                </button>
            </div>

        </div>
    </div>
</template>

<script setup>
import ComeScenario from '@/components/ComeScenario.vue';
import { useAccountStore } from '@/stores/accountStore';
import { useGameStore, useMovieStore, useUserStore } from '@/stores/counter';
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter()
const useraction = ref(null)
const moviestore = useMovieStore()
const gamestore = useGameStore()
const accountstore = useAccountStore()


let today = new Date()
let year = today.getFullYear()
let month = today.getMonth() + 1
let day = today.getDate()

const result = ref(router.options.history.state.result)
const nextStage = function () {
    gamestore.game_round++;
    if (gamestore.game_round > 4) {
        router.push({ name: 'ResultPage' }); // 여기에 결과 페이지의 라우트 이름을 사용하세요.
    }
    else {
        // game round 번째 시나리오가 오는 중입니다.
        router.push({ name: 'loading', query: { next_problem: result.value.next_problem } })

    }
    // 여기에 넣을겨
}




</script>

<style scoped>


.description-box {
    border: 2px solid var(--abbey);
    border-radius: 10px;
    background-color: black;
    color: white;
    width: fit-content;
    margin: 32px 0px;
    padding: 16px 32px;
}

.high-bar {
    background-color: var(--black06);
    border: 1px solid var(--abbey);
    border-radius: 15px;
    padding: 1.5rem;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.bar-content {
    display: grid;
    grid-template-columns: 1fr 4fr 2fr;
    gap: 2rem;
    align-items: center;
}

/* 라운드 섹션 */
.round-circle {
    width: 80px;
    height: 80px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin: 0 auto;
}


.round-number {
    font-size: 2rem;
    font-weight: 700;
    color: white;
}

/* 진행 상황 섹션 */
.progress-section {
    padding: 0 1rem;
}

.date-display {
    font-size: larger;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    color: #FFFFFF;
    font-weight: 500;
    margin-bottom: 1rem;
    padding: 0.5rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.date-display i {
    color: var(--red45);
}

.progress-indicators {
    display: flex;
    justify-content: center;
    gap: 0.8rem;
    padding: 0.5rem 0;
}

.progress-dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.1);
    transition: all 0.3s ease;
}

.progress-dot.active {
    background: var(--red45);
    box-shadow: 0 0 10px rgba(131, 2, 19, 0.5);
}

/* 정보 섹션 */
.info-section {
    font-size: larger;
    border-left: 1px solid rgba(255, 255, 255, 0.1);
    border-right: 1px solid rgba(255, 255, 255, 0.1);
    padding: 0 2rem;
}

.info-row {
    padding: 0.8rem 1rem;
    display: flex;
    align-items: center;
    gap: 1rem;
}

.info-row:first-child {
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.info-row i {
    color: var(--red45);
    font-size: 1.2rem;
}

.info-label {
    color: var(--grey60);
    font-weight: 500;
    min-width: 60px;
}

.info-value {
    color: #FFFFFF;
    font-weight: 500;
    flex-grow: 1;
    font-size: larger;
}

.bigbig-container {
    padding: 5rem;
    text-align: center;
    background-color: var(--black10);
}

.btn-loc {
    margin-left: 10%;
}

.submit-btn {
    padding: 10px 20px;
    font-size: large;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    color: white;
    background-color: red;
}

.selected {
    color: #2196F3;
}

.discarded {
    color: var(--red45);
}

.playgame-container {
    margin: 20px;
    max-width: 1320px;
    margin: 0 auto
}


/* .scenario-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20%;
    margin-top: 40px;
} */

.scenario-box,
.prompt-box {
    overflow-y: auto;
    padding: 20px;
    font-size: medium;
    border-radius: 10px;
    background-color: black;
    color: white;
    width: 400px;
    height: 500px;
    text-align: center;
    /* 내부 텍스트를 가운데 정렬 */
}

.prompt-box {
    background-color: gray;
    /* prompt-box만 다른 배경색으로 설정 */
}

/* 결과 섹션 스타일링 */

.description-box {
    background-color: var(--black06);
    border: 1px solid var(--abbey);
    border-radius: 12px;
    padding: 1rem 2rem;
    margin: 2rem auto;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    width: auto;
    display: inline-block;
}

.description-box span {
    /* padding: 0.5rem 1.5rem; */
    border-radius: 24px;
    font-weight: 600;
    font-size: larger;
}

.description-box span[style*="blue"] {
    background: rgba(0, 122, 255, 0.1);
    border: 1px solid rgba(0, 122, 255, 0.3);
}

.description-box span[style*="red"] {
    background: rgba(131, 2, 19, 0.1);
    border: 1px solid rgba(131, 2, 19, 0.3);
}

/* 시나리오 컨테이너 */
.scenario-container {
    display: flex;
    justify-content: center;
    gap: 3rem;
    margin: 2rem auto;
    max-width: 1200px;
}

.scenario-box,
.prompt-box {
    flex: 1;
    background-color: var(--black06);
    border: 1px solid var(--abbey);
    border-radius: 15px;
    padding: 1.5rem;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    height: 500px;
    display: flex;
    flex-direction: column;
    max-width: 500px;
}

.scenario-box::before {
    content: '유저 시나리오';
    color: #FFFFFF;
    font-weight: 600;
    font-size: 1.2rem;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.prompt-box::before {
    content: '평가 결과';
    color: #FFFFFF;
    font-weight: 600;
    font-size: 1.2rem;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.scenario-result{
    padding: 0px;
}


.scenario-box p,
.prompt-box p {
    flex-grow: 1;
    overflow-y: auto;
    overflow-x: auto;
    padding: 1rem;
    margin: 0;
    text-align: left;
    line-height: 1.6;
    background: rgba(0, 0, 0, 0.2);
    border-radius: 8px;
    color: #FFFFFF;
}

/* 다음 버튼 */
.btn.btn-danger {
    background-color: var(--black06);
    color: white;
    padding: 0.8rem 1.5rem;
    border: 2px solid var(--red45);
    border-radius: 8px;
    font-size: 1.1rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.8rem;
    transition: all 0.3s ease;
}

.btn.btn-danger:hover {
    background-color: var(--red45);
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(131, 2, 19, 0.4);
}

/* 스크롤바 스타일링 */
.scenario-box p::-webkit-scrollbar,
.prompt-box p::-webkit-scrollbar {
    width: 6px;
}

.scenario-box p::-webkit-scrollbar-track,
.prompt-box p::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 3px;
}

.scenario-box p::-webkit-scrollbar-thumb,
.prompt-box p::-webkit-scrollbar-thumb {
    background: var(--red45);
    border-radius: 3px;
}
</style>