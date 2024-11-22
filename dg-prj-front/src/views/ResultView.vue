<template>
    <div class="bigbig-container">

        <!-- <h1>최종 결과 페이지</h1> -->
        <div class="page-header">
            <h1 class="title">
                <span class="title-main">최종 결과</span>
                <span class="title-sub" style="font-size: xx-large;">FINAL RESULT</span>
            </h1>
        </div>
        
        <!-- 모달 -->
        <!-- Button trigger modal -->
        <button type="button" class="recommend-btn" :disabled="!recommend" data-bs-toggle="modal"
            data-bs-target="#staticBackdrop" @click="recommend_toggle">
            <i class="bi bi-film"></i>
            영화 추천 받기
        </button>

        <!-- Modal -->
        <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
            aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog modal-lg modal-dialog-centered modal-dialog-scrollable">

                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="staticBackdropLabel">영화 추천</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body" v-if="recommend_info" style="color: black;">
                        <h3> 스토리 요약</h3>
                        <p> {{ recommend.story_summary }}</p>
                        <hr>
                        <h3>감정 분석</h3>
                        <p>{{ recommend.psychological_analysis }}</p>
                        <hr>
                        <h3>영화 추천</h3>
                        <img :src="`https://image.tmdb.org/t/p/w400${recommend_info.results[0].poster_path}`"
                            alt="추천 영화 포스터" v-if="recommend_info.results[0].poster_path">
                        <img class="poster" src='@/assets/selectimg.jpeg' v-else><br>

                        <!-- <img :src="`https://image.tmdb.org/t/p/w$400/z7ilT5rNN9kDo8JZmgyhM6ej2xv.jpg/`" alt=""> -->
                        <p>제목 : {{ recommend.recommended_movie.title }}</p>
                        <p>추천 이유 : {{ recommend.recommended_movie.reason }}</p>
                        <p>테마 : {{ recommend.recommended_movie.theme }}</p>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
                        <button type="button" class="btn btn-primary">Understood</button>
                    </div>
                </div>
            </div>
        </div>


        <div v-if="!result">로딩 중 입니다..</div>
        <div v-else class="history-container">
            <div v-for="(res, index) in result.history" :key="index">
                <div v-if="index > 0" class="round-card">
                    <!-- 라운드 헤더 -->
                    <div class="round-header">
                        <span class="round-number">ROUND {{ index }}</span>
                    </div>

                    <!-- 라운드 컨텐츠 -->
                    <div class="round-content">
                        <!-- 상황 섹션 -->
                        <div class="content-section">
                            <h5 class="section-title">
                                <i class="bi bi-bookmark-fill"></i> 상황
                            </h5>
                            <div class="section-text">{{ res.situation }}</div>
                        </div>

                        <!-- 답변 섹션 -->
                        <div class="content-section">
                            <h5 class="section-title">
                                <i class="bi bi-chat-square-text-fill"></i> 나의 선택
                            </h5>
                            <div class="section-text">{{ res.user_action }}</div>
                        </div>

                        <!-- 평가 섹션 -->
                        <div class="content-section">
                            <h5 class="section-title">
                                <i class="bi bi-star-fill"></i> 평가
                            </h5>
                            <div class="evaluation-box">
                                <div class="evaluation-result">{{ res.evaluation }}</div>
                                <div class="evaluation-reason">{{ res.reason }}</div>
                            </div>
                        </div>

                        <!-- 결과 섹션 -->
                        <div class="content-section">
                            <h5 class="section-title">
                                <i class="bi bi-flag-fill"></i> 결과
                            </h5>
                            <div class="section-text">{{ res.next_situation }}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/accountStore';
import { useGameStore, useUserStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted, ref } from 'vue';
const result = ref()
const gamestore = useGameStore()
const userstore = useUserStore()
const isRecommend = ref(false)
const recommend = ref(null)
const recommend_info = ref(null)
const accountstore = useAccountStore()



const recommend_toggle = function () {
    isRecommend.value = !isRecommend.value
    console.log(result.value)


}

onMounted(() => {
    console.log('gamenum:', gamestore.game_id)
    axios({
        method: 'get',
        url: `http://127.0.0.1:8000/gameApp/record/${gamestore.game_id}/`,
        headers: {
            Authorization: `Token ${accountstore.token}`,

        }
    })
        .then(res => {
            console.log(res.data); // 이러면 JSON 문자열 그대로 반환됨. 
            result.value = res.data;

            // history가 JSON 문자열인 경우 파싱
            if (typeof res.data.history === 'string') {
                res.data.history = JSON.parse(res.data.history); // 그래서 파싱 해줌.
            }
            // result.value = res.data; 
        }).then(res => {
            // 영화 추천 및 감정분석을 위한 axios 호출.
            axios({
                method: 'post',
                url: `http://127.0.0.1:8000/gameApp/recommend/${gamestore.game_id}/`,
                headers: {
                    Authorization: `Token ${accountstore.token}`,
                    "Content-Type": "application/json"
                },
                data: {
                    result: result.value
                }
            }).then(res => {
                console.log(res)
                recommend.value = res.data.result
            })
                .then(res => {
                    // 추천 받은 영화 정보를 받아와야 함. 그래서 TMDB에 axios 보낼거임.
                    axios({
                        method: 'get',
                        url: `https://api.themoviedb.org/3/search/movie`,
                        headers: {
                            accept: 'application/json',
                            Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNmFmOGIwNGUyZTI0MTgwZGQ5NTgxMTFhOWIwMzVkOCIsIm5iZiI6MTczMjE3NDI2Ny45MTU4ODEsInN1YiI6IjY3MjEwNWE2NGJlMTU0NjllNzBlNzhkMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Hn679BEcxrEDiQhMZmHkI0oJlM93CpNmgDVxNlUwBWM'
                        },
                        params: {
                            include_adult: true,
                            language: "ko-KR",
                            page: 1,
                            query: recommend.value.recommended_movie.title,
                        }
                    }).then(res => {
                        console.log('ggg', res)
                        recommend_info.value = res.data

                    })
                })
        })
        .catch(err => console.log(err))
})

</script>

<style scoped>
.page-header {
    text-align: center;
    padding: 2rem 0 3rem 0;
    margin-bottom: 2rem;
    position: relative;
}

.title {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
}

.title-main {
    color: #1A1A1A;
    font-size: 2.8rem;
    font-weight: 700;
    letter-spacing: 2px;
    position: relative;
    padding-bottom: 0.5rem;
}

.title-main::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 60px;
    height: 4px;
    background-color: #830213;
}

.title-sub {
    color: #8B8680;
    font-size: 1rem;
    letter-spacing: 5px;
    font-weight: 500;
}

/* 반응형 디자인 */
@media (max-width: 768px) {
    .title-main {
        font-size: 2rem;
    }
    
    .title-sub {
        font-size: 0.9rem;
    }
}

/* 선택적: 애니메이션 효과 추가 */
@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.page-header {
    animation: slideIn 0.8s ease-out;
}
.recommend-btn {
    background-color: #1A1A1A;
    color: #ffffff;
    padding: 0.8rem 1.5rem;
    border: 2px solid #830213;
    border-radius: 8px;
    font-weight: 600;
    font-size: 1.1rem;
    transition: all 0.3s ease;

    align-items: center;
    gap: 0.5rem;
}

.recommend-btn:hover:not(:disabled) {
    background-color: #830213;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.recommend-btn:disabled {
    background-color: #8B8680;
    border-color: #8B8680;
    cursor: not-allowed;
    opacity: 0.7;
}

.recommend-btn i {
    font-size: 1.2rem;
}

.bigbig-container {
    padding: 5rem;
    text-align: center;
}

.result-content {
    font-size: smaller;
}

p {
    font-size: smaller;
}

.history-container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 20px;

}

.round-card {
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    margin-bottom: 2rem;
    border-top: 4px solid #830213;
    transition: transform 0.2s ease;
}

.round-card:hover {
    transform: translateY(-5px);
}

.round-header {
    background-color: black;
    padding: 1rem 1.5rem;
    border-radius: 6px 6px 0 0;
}

.round-number {
    color: #ffffff;
    font-weight: 600;
    font-size: 1.2rem;
    letter-spacing: 1px;
}

.round-content {
    padding: 1.5rem;
}

.content-section {
    margin-bottom: 1.5rem;
    padding: 1rem;
    background-color: #f8f8f8;
    border-radius: 8px;
    border-left: 4px solid #8B8680;
}

.section-title {
    color: #1A1A1A;
    font-weight: 600;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.section-title i {
    color: #830213;
}

.section-text {
    color: #333333;
    line-height: 1.6;
    font-size: 0.95rem;
}

.evaluation-box {
    background-color: #ffffff;
    padding: 1rem;
    border-radius: 6px;
    border-left: 4px solid #830213;
}

.evaluation-result {
    font-weight: 600;
    color: #830213;
    margin-bottom: 0.5rem;
}

.evaluation-reason {
    color: #666666;
    font-size: 0.9rem;
    line-height: 1.5;
}

/* 반응형 디자인 */
@media (max-width: 768px) {
    .history-container {
        padding: 10px;
    }

    .round-content {
        padding: 1rem;
    }

    .content-section {
        padding: 0.8rem;
    }
}
</style>