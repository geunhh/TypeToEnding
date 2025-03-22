<template>
    <div class="create-container">
        <div class="form-wrapper">
            <h1 class="page-title">
                <i class="bi bi-film"></i>
                영화 생성 페이지
            </h1>
            <hr class="divider">

            <form @submit.prevent="submitFunc" class="create-form">
                <div class="form-section">
                    <div class="form-group">
                        <label>제목</label>
                        <input type="text" v-model="new_title" class="form-input" placeholder="영화 제목을 입력하세요">
                    </div>

                    <div class="form-group">
                        <label>줄거리</label>
                        <textarea v-model="new_description" class="form-textarea"
                            placeholder="영화의 줄거리를 입력하세요 "></textarea>
                    </div>

                    <div class="form-group">
                        <label>세계관</label>
                        <textarea v-model="new_context" class="form-textarea" placeholder="영화의 세계관을 설명해주세요"></textarea>
                    </div>
                </div>

                <div class="form-section">
                    <div class="form-group">
                        <label>초기 상황 1</label>
                        <textarea v-model="new_situation1" class="form-textarea" placeholder="초기 상황을 설명해주세요
게임의 초기 상황으로 부여됩니다"></textarea>
                    </div>
                    <div style="min-height: 120px;">
                        <div class="collapse collapse-horizontal " id="collapseWidthExample">
                            <div class="card card-body description">
                                <h5>1. 세계관 작성</h5>
                                <p>영화의 배경과 이야기가 진행되는 환경을 설정하세요.</p>
                                세계관은 시나리오의 전체적인 흐름의 기반이 되는 요소로
                                <hr class="tip-divider">
                                <h5>2. 줄거리 작성</h5>
                                <p>주요 인물의 목표와 사건을 중심으로 줄거리를 만드세요.</p>
                                <ul>
                                    <li>주인공이 전설적인 검을 찾아 세계를 구하려는 이야기</li>
                                    <li>AI에 의해 통제되는 미래에서 자유를 되찾기 위한 혁명</li>
                                </ul>
                                <hr class="tip-divider">
                                <h5>3. 초기 상황 작성</h5>
                                <p>게임의 시작 상황과 플레이어가 직면한 문제를 구체적으로 설명하세요.</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <button type="submit" class="btn-primary">
                        <i class="bi bi-plus-circle"></i>
                        영화 생성하기
                    </button>
                    <p style="margin-top: 16vh;">
                        <button class="btn-secondary" type="button" data-bs-toggle="collapse"
                            data-bs-target="#collapseWidthExample" aria-expanded="false"
                            aria-controls="collapseWidthExample">
                            영화 생성 Tip.
                        </button>
                    </p>
                    <button @click="gohome" class="btn-secondary">뒤로가기</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/accountStore';
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()
const new_title = ref(null)
const new_description = ref(null)
const new_context = ref(null)
const accountstore = useAccountStore()
const new_situation1 = ref(null)

const gohome = function () {
    router.push({ name: 'main' })
}
const submitFunc = function () {
    // 각각의 칸 체크
    if (!new_title.value || !new_context.value || !new_description.value
        || !new_situation1.value) {
        alert('모든 항목을 입력해주세요.')
        return
    }
    if (new_description.value.length < 20) {
        alert('줄거리는 최소 20글자 이상 입력해주세요.')
        return
    }
    if (new_context.value.length < 20) {
        alert('세계관은 최소 20글자 이상 입력해주세요.');
        return;
    }
    if (new_situation1.value.length < 20) {
        alert('초기 상황은 최소 20글자 이상 입력해주세요.');
        return;
    }
    // 영화 제작     
    axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/gameApp/movielist/',
        headers: {
            Authorization: `Token ${accountstore.token}`
        },
        data: {
            title: new_title.value,
            description: new_description.value,
            context: new_context.value,
            creator: accountstore.userId
        }

    })
        // 영화 제작 후 초기 질문 제작
        .then(res => {
            console.log(res)
            axios({
                method: 'post',
                url: 'http://127.0.0.1:8000/gameApp/initialquestion/',
                headers: {
                    Authorization: `Token ${accountstore.token}`
                },
                data: {
                    movie: res.data.id,
                    question: new_situation1.value
                }
            })
        })
        .then(res => {
            console.log(res)
            console.log('영화 및 질문 제작 성공')
            alert('커스텀 영화 제작에 성공했습니다. 메인페이지로 돌아갑니다.')
            router.push({ name: 'main' })
        })
        .catch(err => console.log(err))

}

</script>

<style scoped>
/* 공통 버튼 스타일 */
button {
    font-family: 'Manrope', sans-serif;
    font-size: 1rem;
    font-weight: 500;
    border-radius: 8px;
    padding: 0.8rem 1.5rem;
    cursor: pointer;
    transition: all 0.3s ease-in-out;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.8rem;
    border: none;
}

/* 기본 버튼 스타일 */
button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

/* Primary 버튼 (강조된 스타일) */
.btn-primary {
    background-color: var(--black10);
    color: #FFFFFF;
    border: 2px solid var(--red45);
}

.btn-primary:hover {
    background: var(--red45)
}

/* Secondary 버튼 (보조 스타일) */
.btn-secondary {
    background: var(--black10);
    color: #FFFFFF;
    border: 1px solid var(--grey60);
    transition: all 0.3s ease;
}

.btn-secondary:hover {
    background: var(--grey60);
}

/* 버튼 크기 조정 */
button i {
    font-size: 1.2rem;
    color: inherit;
}

/* 모바일 반응형 */
@media (max-width: 768px) {
    button {
        font-size: 0.9rem;
        padding: 0.6rem 1.2rem;
    }

    button i {
        font-size: 1rem;
    }
}

.tip-divider {
    border: none;
    border-top: 1px solid rgba(255, 255, 255, 0.2);
    margin: 1rem 0;
}

.description {
    border: 1px solid var(--black15);
    max-height: 32vh;
    overflow-y: auto;
    border-radius: 10px;
    background-color: var(--black10);
    font-size: small;
    padding: 1rem;
    scrollbar-width: thin;
    scrollbar-color: var(--red45) transparent;
    max-height: 18rem;
}

/* 크롬, Edge, Safari용 스크롤바 커스터마이징 */
.description::-webkit-scrollbar {
    width: 8px;
    /* 스크롤바 너비 */
}

.description::-webkit-scrollbar-track {
    background: transparent;
    /* 트랙 배경 */
}

.description::-webkit-scrollbar-thumb {
    background: var(--red45);
    /* 스크롤바 색상 */
    border-radius: 10px;
    /* 둥근 모서리 */
}

.description::-webkit-scrollbar-thumb:hover {
    background: var(--red45);
    /* 스크롤바 호버 시 색상 */
}


.create-container {
    padding: 3rem;
    background: var(--black10);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.form-wrapper {
    background: var(--black06);
    border: 1px solid var(--abbey);
    border-radius: 15px;
    padding: 2.5rem;
    width: 100%;
    max-width: 1200px;
    box-shadow: 0 4px 15px var(--black10);
}

.page-title {
    color: #FFFFFF;
    font-size: 2rem;
    margin-bottom: 1rem;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
}

.form-textarea {
    min-height: 200px;
    /* 텍스트 영역 높이 증가 */
    resize: vertical;
    line-height: 1.6;
    font-size: 1rem;
    resize: none;
    background: var(--black10);
}

.page-title i {
    color: var(--red45);
}

.divider {
    border: none;
    height: 2px;
    background: var(--red45);
    margin: 1.5rem 0;
}

.create-form {
    display: flex;
    gap: 2rem;
}

.form-section {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.form-group label {
    color: var(--grey60);
    font-weight: 500;
}

.form-group textarea[v-model="new_context"],
.form-group textarea[v-model="new_situation1"] {
    min-height: 300px;
    resize: none
}

.form-input,
.form-textarea {
    background: var(--black10);
    border: 1px solid var(--abbey);
    border-radius: 8px;
    padding: 0.8rem;
    color: #FFFFFF;
    font-size: 1rem;
    transition: all 0.3s ease;
    resize: none
}

.form-textarea {
    min-height: 150px;
    resize: vertical;
    resize: none
}

.form-input:focus,
.form-textarea:focus {
    outline: none;
    border-color: var(--red45);
    box-shadow: 0 0 0 2px rgba(131, 2, 19, 0.2);
}

.submit-btn {
    background-color: var(--red45);
    color: white;
    padding: 0.8rem 1.5rem;
    /* 버튼 패딩 축소 */
    border: none;
    border-radius: 8px;
    font-size: 1rem;
    /* 폰트 크기 축소 */
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    display: inline-flex;
    /* 인라인 플렉스로 변경 */
    align-items: center;
    justify-content: center;
    gap: 0.8rem;
    margin-top: 2rem;
    width: auto;
    /* 자동 너비로 변경 */
    height: 2rem;
}

.submit-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(131, 2, 19, 0.4);
}

@media (max-width: 768px) {
    .create-container {
        padding: 1rem;
    }

    .create-form {
        flex-direction: column;
    }
}
</style>