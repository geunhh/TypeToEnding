<template>
    <div>
        <!-- 모달 -->
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
                            alt="추천 영화 포스터" v-if="recommend_info.results.length > 0">
                        <img class="poster" src='@/assets/posters/NoPoster.png' v-else><br>

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

        <!-- 댓글 모달 -->
        <div class="modal fade" id="commentModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header comment-modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">재밌게 플레이하셨나요? 후기로 댓글을 남겨주세요</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body comment-modal-body">
                        <div>
                            <div class="mb-3">
                                <input v-model="userComment" type="text" class="form-control comment-modal-form"
                                    id="message-text" @keyup.enter="sendComment">
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer comment-modal-footer">
                        <button type="button" class="btn btn-primary leave-comment" @click.prevent="sendComment">댓글
                            남기기</button>
                        <button type="button" class="btn btn-secondary comment-close"
                            data-bs-dismiss="modal">닫기</button>
                    </div>
                </div>
            </div>
        </div>



    </div>
    <div v-if="!result">로딩 중 입니다...</div>
    <div v-else class="new-result-container-main">
        <div class="new-result-container-rounds">
            <div class="new-result-header">
                <p class="new-result-final-result">최종 결과</p>
            </div>
            <div class="new-result-container">
                <div class="new-result-result" v-for="(res, index) in result.history" :key="index">
                    <div class="new-result-round" v-if="index > 0">{{ index }}</div>
                    <div class="new-result-paragraph" v-if="index > 0">
                        <div class="new-result-evaluation">
                            <img v-if="res.evaluation === '적절함'" class="new-result-selected-or-discarded"
                                src="@/assets/icons/selected.png" alt="selected">
                            <img v-else class="new-result-selected-or-discarded" src="@/assets/icons/discarded.png"
                                alt="discarded">
                        </div>
                        <p class="category-heading">상황</p>
                        <p class="category-paragraph">{{ res.situation }}</p>
                        <p class="category-heading">당신의 대답</p>
                        <p class="category-paragraph">{{ res.user_action }}</p>
                        <p class="category-heading">이유</p>
                        <p class="category-paragraph">{{ res.reason }}</p>
                        <p class="category-heading">결과</p>
                        <p class="category-paragraph">{{ res.next_situation }}</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="new-result-recommend-summary-button">
            <div class="new-result-recommend-summary">
                <div class="buttons">
                    <button type="button" class="recommend-btn" :disabled="!recommend" @click="isRecommend = true">
                        <i class="bi bi-film"></i>
                        영화 추천 받기
                    </button>




                    <button type="button" class="comment-btn" data-bs-toggle="modal" data-bs-target="#commentModal">
                        <i class="bi bi-chat-left-dots-fill"></i> 댓글 남기기
                    </button>



                </div>
                <div class="new-result-movie-recommendation" v-if="isRecommend">
                    <p class="category-heading"> 스토리 요약</p>
                    <p class="category-paragraph"> {{ recommend.story_summary }}</p>
                    <hr>
                    <p class="category-heading">감정 분석</p>
                    <p class="category-paragraph">{{ recommend.psychological_analysis }}</p>
                    <hr>
                    <p class="category-heading">영화 추천</p>
                    <img :src="`https://image.tmdb.org/t/p/w400${recommend_info.results[0].poster_path}`"
                        alt="추천 영화 포스터" v-if="recommend_info.results.length!=0">
                    <img class="poster" src='@/assets/selectimg.jpeg' style="width: 400px;" v-else><br>
                    <br>
                    <p class="category-heading">제목</p>
                    <p class="category-paragraph"> {{ recommend.recommended_movie.title }}</p>
                    <p class="category-heading">추천 이유</p>
                    <p class="category-paragraph">{{ recommend.recommended_movie.reason }}</p>
                    <p class="category-heading">테마 : </p>
                    <p class="category-paragraph">{{ recommend.recommended_movie.theme }}</p>
                </div>
            </div>
            <button type="button" class="btn btn-primary new-result-to-main" data-bs-toggle="modal"
                data-bs-target="#AreSurelyBackToMain">
                <p class="new-result-to-main-p">메인화면으로</p>
            </button>
        </div>
    </div>

    <!-- 메인화면으로 돌아갈건지 묻는 모달 -->
    <div class="modal fade" id="AreSurelyBackToMain" tabindex="-1" aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content back-to-main-page">
                <div class="modal-header back-to-main-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">정말로 메인화면으로 돌아가시겠습니까?</h1>
                </div>
                <div class="modal-footer back-to-main-footer">
                    <button type="button" class="btn btn-primary yes" @click="backToMain" data-bs-dismiss="modal">
                        <p class="choose-back-to-main">네 메인화면으로 갈래요</p>
                    </button>
                    <button type="button" class="btn btn-primary no" data-bs-dismiss="modal">
                        <p class="choose-back-to-main">아뇨 여기 남아있을게요</p>
                    </button>
                </div>
            </div>
        </div>
    </div>

</template>

<script setup>
import { useAccountStore } from '@/stores/accountStore';
import { useGameStore, useMovieStore, useUserStore } from '@/stores/counter';
import axios from 'axios';
// import { send } from 'vite';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
const TMDB_API_KEY = import.meta.env.TMDB_API_KEY

const result = ref()
const router = useRouter()
const gamestore = useGameStore()
const userstore = useUserStore()
const isRecommend = ref(false)
const recommend = ref(null)
const recommend_info = ref(null)
const movieStore = useMovieStore()
const accountstore = useAccountStore()
const userComment = ref('')
const BASE_URL = accountstore.BASE_URL


onMounted(() => {
    // 먼저 game_id 에 해당하는 record 가져와야 해
    axios({                 
        method: 'get',
        url: `http://127.0.0.1:8000/gameApp/record/${gamestore.game_id}/`,
        headers: {
            Authorization: `Token ${accountstore.token}`,            
        }
    })
    // 다음은 record를 분석 및 추천 알고리즘에 보내.
    .then(res => {
        result.value = res.data;
        
        // history가 JSON 문자열인 경우 파싱
        if (typeof res.data.history === 'string') {
            res.data.history = JSON.parse(res.data.history); // 그래서 파싱 해줌.
        }
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
            recommend.value = res.data.result
        }).then(res => {              
            // 추천 받은 영화 정보를 받아와야 함. 그래서 TMDB에 axios 보낼거임.
            axios({
                method: 'get',
                url: `https://api.themoviedb.org/3/search/movie`,
                headers: {
                    accept: 'application/json',
                    Authorization: `Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNmFmOGIwNGUyZTI0MTgwZGQ5NTgxMTFhOWIwMzVkOCIsIm5iZiI6MTczMjE3NDI2Ny45MTU4ODEsInN1YiI6IjY3MjEwNWE2NGJlMTU0NjllNzBlNzhkMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Hn679BEcxrEDiQhMZmHkI0oJlM93CpNmgDVxNlUwBWM`
                },
                params: {
                    include_adult: true,
                    language: "ko-KR",
                    page: 1,
                    query: recommend.value.recommended_movie.title,
                }
            }).then(res => {
                recommend_info.value = res.data
                console.log(recommend_info)
            })

        })
    })
    .catch(err => console.log(err))

})


// 메인 화면으로 돌아가주는 함수
const backToMain = () => {
    router.push({ name: 'main' })
}

// 플레이했던 영화에 댓글을 남기는 함수
const sendComment = () => {
    // console.log(movieStore.movieId)
    if (userComment.value) {
        axios({
            method: 'POST',
            url: `http://127.0.0.1:8000/gameApp/comment/${movieStore.movieId}/`,
            headers: {
                Authorization: `Token ${accountstore.token}`,
                "Content-Type": "application/json"
            },
            data: { content: userComment.value }
        }).then(res => {
            // console.log(userComment.value)
            window.alert('댓글이 작성되었습니다.')
        }
        ).catch(err => window.alert('댓글을 남기는데 실패했습니다'))
    } else {
        window.alert('내용을 작성해주세요')
    }
    userComment.value = ""
}

</script>


<style scoped>
.title {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
}

.comment-btn {
    border: 2px solid var(--red45);
    background-color: var(--black10);
    transition: all 0.3s ease;
    border-radius: 8px;
    padding: 0.8rem 1.5rem;
    color: #ffffff;
    font-weight: 600;
    font-size: 1.1rem;
    transition: all 0.3s ease;
    align-items: center;
    gap: 0.5rem;
}

.comment-btn:hover {
    background-color: var(--red45);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
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

.buttons {
    display: flex;
    justify-content: space-between;
    gap: 50px;
}

.recommend-btn {
    background-color: var(--black10);
    color: #ffffff;
    padding: 0.8rem 1.5rem;
    border: 2px solid var(--red45);
    border-radius: 8px;
    font-weight: 600;
    font-size: 1.1rem;
    transition: all 0.3s ease;

    align-items: center;
    gap: 0.5rem;
}

.recommend-btn:hover:not(:disabled) {
    background-color: var(--red45);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.recommend-btn:disabled {
    background-color: var(--grey60);
    border-color: var(--grey60);
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
    border-top: 4px solid var(--red45);
    transition: transform 0.2s ease;
}

.round-card:hover {
    transform: translateY(-5px);
}


.round-content {
    padding: 1.5rem;
}

.content-section {
    margin-bottom: 1.5rem;
    padding: 1rem;
    background-color: #FFFFFF;
    border-radius: 8px;
    border-left: 4px solid var(--grey60);
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

.new-result-final-result {
    font-size: 40px;
    font-family: 'Gowun Dodum', sans-serif;
    margin-bottom: 0px;
}

.new-result-container-main {
    align-items: flex-start;
    background-color: var(--black10);
    display: flex;
    gap: 71px;
    height: 100%;
    padding: 31px 35px;
    width: 100%;
    color: #ffffff;
    justify-content: center;
}

.new-result-to-main-p {
    color: #FFFFFF;
    margin-bottom: 0px;
    font-family: var(--font-family-manrope);
    font-size: 20px;
}

.new-result-container-rounds {
    align-items: flex-start;
    background-color: var(--black06);
    border: 1px solid;
    border-color: var(--black15);
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    gap: 30px;
    height: 960px;
    padding: 50px;
    width: 755px;
    overflow: hidden;
}

.new-result-header {
    display: flex;
    justify-content: center;
    width: 100%;
}

.new-result-container {
    overflow-y: auto;
    max-height: calc(100% - 80px);
    width: 100%;
}

.new-result-result {
    align-items: center;
    align-self: stretch;
    border-bottom-style: solid;
    border-bottom-width: 1px;
    border-color: var(--black15);
    border-top-style: solid;
    border-top-width: 1px;
    display: flex;
    flex: 0 0 auto;
    gap: 20px;
    padding: 20px 0px;
    position: relative;
    width: 100%;
}

.new-result-round {
    color: var(--grey60);
    font-family: var(--font-family-manrope);
    font-weight: 600;
    letter-spacing: 0;
    width: 60px;
    text-align: center;
    height: 100%;
    font-size: 40px;
    flex-shrink: 0;
}

.new-result-paragraph {
    color: var(--grey60);
    font-family: var(--profile-font-family-manrope);
    font-size: var(--profile-font-size-m);
    font-style: normal;
    font-weight: 400;
    flex-grow: 1;
    overflow-wrap: break-word;
    word-wrap: break-word;
    hyphens: auto;
}

.new-result-evaluation {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    margin-bottom: 20px;
    height: 100%;
}

.new-result-selected-or-discarded {
    width: 80px;
    height: 40px;
    flex-shrink: 0;
    margin-top: 0;

}

.category-heading {
    color: var(--absolutewhite);
    font-size: var(--font-size-m);
    font-weight: 600;
    line-height: 30px;
    font-family: 'Gowun Dodum', sans-serif;
    letter-spacing: 0;
    position: relative;
    margin-bottom: 5px;
}

.category-paragraph {
    color: var(--grey60);
    font-family: 'Gowun Dodum', sans-serif;
}

.new-result-recommend-summary-button {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin-top: 1px;
    gap: 50px;
    min-height: 942px;
    width: 500px;
}

.new-result-recommend-summary {
    align-items: flex-start;
    background-color: var(--black06);
    border: 1px solid;
    border-color: var(--black15);
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    height: 843px;
    padding: 40px;
    width: 500px;
    gap: 20px;
}

.btn.btn-primary.leave-comment {
    background-color: var(--black06);
    border: 2px solid var(--red45);
    transition: all 0.3s ease;
    margin-right: 20px;
}

.btn.btn-primary.leave-comment:hover {
    background-color: var(--red45);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.btn.btn-secondary.comment-close {
    background-color: var(--black06);
    border: 2px solid var(--grey60);
    transition: all 0.3s ease;
}

.btn.btn-secondary.comment-close:hover {
    background-color: var(--grey60);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.btn.btn-primary.new-result-to-main {
    align-items: center;
    background-color: var(--black06);
    border: 2px solid var(--red45);
    border-radius: 8px;
    display: flex;
    justify-content: center;
    padding: 18px 0px;
    width: 496px;
    /* width: 100%; */
    color: #FFFFFF;
    transition: all 0.3s ease;
}

.btn.btn-primary.new-result-to-main:hover {
    background-color: var(--red45);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.choose-back-to-main {
    margin-bottom: 0px;
}

.new-result-movie-recommendation {
    overflow-y: auto;
}

.modal-content.back-to-main-page {
    background-color: var(--black10);
}

.modal-content.back-to-main-page {
    background-color: var(--black06);
    border: 1px solid var(--black15);
}

.modal-header.comment-modal-header,
.modal-header.back-to-main-header,
.modal-footer.back-to-main-footer {
    background-color: var(--black06);
    border: 1px solid var(--black15);
    text-align: center;
    justify-content: center;
}

.modal-body.comment-modal-body {
    background-color: var(--black06);
    border: 1px solid var(--black15);
}

.form-control.comment-modal-form {
    background-color: var(--black06);
    color: #FFFFFF;
    border: 2px solid var(--black15);
}

.modal-footer.comment-modal-footer {
    background-color: var(--black06);
    border: 1px solid var(--black15);
    /* justify-content: center; */
}

.modal-footer.back-to-main-footer {
    display: flex;
    gap: 24px;
    justify-content: space-between;
}

.btn.btn-primary.yes {
    flex: 1;
    max-width: calc(50% - 5px);
    background-color: var(--black06);
    border: 2px solid var(--red45);
    transition: all 0.3s ease;
}

.btn.btn-primary.no {
    flex: 1;
    max-width: calc(50% - 5px);
    background-color: var(--black06);
    border: 2px solid var(--grey60);
    transition: all 0.3s ease;
}


.btn.btn-primary.yes:hover {
    background-color: var(--red45);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}


.btn.btn-primary.no:hover {
    background-color: var(--grey60);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* 스크롤 바 */
/* 옵션 3: 미니멀 컨셉 */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: rgba(26, 26, 26, 0.5);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb {
    background: var(--red45);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--red45);
}
</style>