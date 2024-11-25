<template>
    <div class="bigbig-container">
        <div class="playgame-container container text-center">
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
            <div class="description-game">
                <h4> 주어진 상황에 이어질 시나리오를 작성하시오</h4>
            </div>
            <div class="scenario-container">
                <div class="scenario-box" style="font-size: larger;">
                    <p>시나리오 설명창</p>
                    <p class="scenario-p" v-if="gamestore.next_situation">{{ gamestore.next_situation }}</p>
                    <p class="scenario-p" v-else>{{ gamestore.initial_question }}</p>
                </div>

                <div class="prompt-box">
                    <p>시나리오 작성창 </p>
                    <textarea style="width: 100%; height: 90%; background-color: darkgray;" v-model="useraction">
                </textarea>
                </div>

            </div>
            <button class="submit-btn" @click="goEval" style="margin-top: 30px;">
                시나리오 제출
            </button>

        </div>
    </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/accountStore';
import { useGameStore, useMovieStore, useUserStore } from '@/stores/counter';
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter()
const useraction = ref(null)
const moviestore = useMovieStore()
const gamestore = useGameStore()
const userstore = useUserStore()
const accountstore = useAccountStore()
let today = new Date()
let year = today.getFullYear()
let month = today.getMonth() + 1
let day = today.getDate()




const goEval = function () {
    if (useraction.value.length < 11) {
        alert('시나리오가 너무 짧습니다.')
    }
    else {
        gamestore.user_action1 = useraction.value
        router.push({ name: 'evaluation' })
    }

}


</script>

<style scoped>
.high-bar {
    background-color: var(--black10);
    border: 1px solid rgba(255, 255, 255, 0.1);
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
}

/* 정보 섹션 */
.info-section {
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
    font-size: larger;
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

/* 반응형 디자인 */
@media (max-width: 768px) {
    .bar-content {
        grid-template-columns: 1fr;
        gap: 1rem;
    }

    .info-section {
        border: none;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        padding: 1rem 0;
    }

    .round-circle {
        margin: 0 auto;
    }
}

.row span {
    padding: 0 2px;
}

.row svg {
    display: inline-block;
    padding: 0;
}



.high-bar {
    border: 1px solid var(--abbey);
    border-radius: 10px;
    background-color: var(--black06);
    color: white;
}

.scenario-container {
    display: flex;
    justify-content: center;
    /* 수평 중앙 정렬 */
    align-items: center;
    /* 수직 중앙 정렬 */
    gap: 20%;
    /* 픽셀 단위로 큰 간격 설정 */
    margin-top: 40px;
    /* 추가 여백 */
}


.scenario-box,
.prompt-box {
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

/* 기존 high-bar 관련 스타일은 유지하고, 아래 스타일을 추가/수정합니다 */

.bigbig-container {
    padding: 3rem;
    background-color: var(--black10);
    min-height: 100vh;
}

.description-game {
    background-color: var(--black06);
    border: 1px solid var(--abbey);
    border-radius: 12px;
    padding: 1rem 2rem;
    margin: 2rem auto;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    width: auto;
    display: inline-block;
}

.description-game h4 {
    color: #FFFFFF;
    font-weight: 500;
    margin: 0;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.description-game h4::before {
    content: '\F4DD';
    font-family: bootstrap-icons;
    color: var(--red45);
    font-size: 1.2rem;
}

.scenario-container {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    gap: 2rem;
    margin-top: 2rem;
}

.scenario-box,
.prompt-box {
    flex: 1;
    max-width: 500px;
    background-color: var(--black06);
    border: 1px solid var(--abbey);
    border-radius: 15px;
    padding: 1.5rem;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    height: 500px;
    display: flex;
    flex-direction: column;
}

.scenario-box p:first-child,
.prompt-box p:first-child {
    color: var(--red45);
    font-weight: 600;
    font-size: 1.1rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.scenario-box p:first-child::before {
    content: '\F4D5';
    font-family: bootstrap-icons;
}

.prompt-box p:first-child::before {
    content: '\F4CB';
    font-family: bootstrap-icons;
}

.scenario-box p:not(:first-child) {
    color: #FFFFFF;
    line-height: 1.6;
    flex-grow: 1;
    overflow-y: auto;
    background: rgba(0, 0, 0, 0.2);
    border-radius: 8px;
    text-align: left;
}

.prompt-box textarea {
    flex-grow: 1;
    background: rgba(0, 0, 0, 0.2);
    border: none;
    border-radius: 8px;
    padding: 1rem;
    color: #FFFFFF;
    font-size: 1rem;
    line-height: 1.6;
    resize: none;
    color: black;
}

.prompt-box textarea:focus {
    outline: 1px solid var(--red45);
}

.submit-btn {
    color: white;
    padding: 1rem 2rem;
    font-size: 1.1rem;
    border: 2px solid var(--red45);
    background-color: var(--black06);
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-top: 2rem;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
}

.submit-btn::before {
    content: '\F4E6';
    font-family: bootstrap-icons;
}

.submit-btn:hover {
    background-color: var(--red45);
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(131, 2, 19, 0.4);
}

/* 스크롤바 스타일링 */
.scenario-box p:not(:first-child)::-webkit-scrollbar,
.prompt-box textarea::-webkit-scrollbar {
    width: 6px;
}

.scenario-box p:not(:first-child)::-webkit-scrollbar-track,
.prompt-box textarea::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 3px;
}

.scenario-box p:not(:first-child)::-webkit-scrollbar-thumb,
.prompt-box textarea::-webkit-scrollbar-thumb {
    background: var(--red45);
    border-radius: 3px;
}
</style>