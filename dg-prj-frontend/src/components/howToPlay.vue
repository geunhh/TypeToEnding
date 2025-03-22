<template>
    <button type="button" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#HowToPlayModal">
        튜토리얼
    </button>

    <div class="modal fade" id="HowToPlayModal" tabindex="-1" aria-labelledby="HowToPlayLabel" aria-hidden="true">
        <div class="modal-dialog modal-xl">
            <div class="modal-content modal-content-htp">
                <div class="modal-header modal-header-htp d-flex justify-content-between align-items-center">
                    <button type="button" class="invisible btn btn-secondary close-btn-htp"
                        data-bs-dismiss="modal">Close</button>
                    <h1 class="modal-title fs-1 m-0 modal-title-htp" id="HowToPlayLabel">튜토리얼</h1>
                    <button type="button" class="btn btn-secondary close-btn-htp" data-bs-dismiss="modal">닫기</button>
                </div>
                <div class="modal-body modal-body-htp modal-body-htp-images">
                    <div id="carouselExampleCaptions" class="carousel slide">
                        <div class="carousel-inner">
                            <div class="carousel-item carousel-item-htp active">
                                <div>
                                    <h2 class="explanation-title-htp">1. 영화 선택</h2>
                                    <p class="explanation-context-htp">대기실에서 플레이할 영화를 선택합니다</p>
                                </div>
                                <img src="@/assets/tutorials/tutorial1.png" class="d-block w-100 howtoimg" alt="1">
                            </div>
                            <div class="carousel-item carousel-item-htp">
                                <div>
                                    <h2 class="explanation-title-htp">2. 시나리오 작성</h2>
                                    <p class="explanation-context-htp">AI가 준비해준 시나리오에 이어질 적절한 시나리오를 작성합니다</p>
                                </div>
                                <img src="@/assets/tutorials/tutorial2.png" class="d-block w-100 howtoimg" alt="2">
                            </div>
                            <div class="carousel-item carousel-item-htp">
                                <div>
                                    <h2 class="explanation-title-htp">3. AI의 평가</h2>
                                    <p class="explanation-context-htp">AI가 당신이 작성한 시나리오를 평가합니다</p>
                                </div>
                                <img src="@/assets/tutorials/tutorial3.png" class="d-block w-100 howtoimg" alt="3">
                            </div>
                            <div class="carousel-item carousel-item-htp">
                                <div>
                                    <h2 class="explanation-title-htp">4. 평가 결과 확인</h2>
                                    <p class="explanation-context-htp">AI의 평가결과에 따라 당신의 시나리오가 채택 혹은 폐기됩니다</p>
                                </div>
                                <img src="@/assets/tutorials/tutorial4.png" class="d-block w-100 howtoimg" alt="4">
                            </div>
                            <div class="carousel-item carousel-item-htp">
                                <div>
                                    <h2 class="explanation-title-htp">5. 최종 결과 확인</h2>
                                    <p class="explanation-context-htp">마지막 라운드가 끝난 후 최종 결과를 확인 할 수 있습니다</p>
                                </div>
                                <img src="@/assets/tutorials/tutorial5.png" class="d-block w-100 howtoimg" alt="5">
                            </div>
                            <div class="carousel-item carousel-item-htp">
                                <div>
                                    <h2 class="explanation-title-htp">6. 영화 추천</h2>
                                    <p class="explanation-context-htp">당신이 작성한 시나리오를 토대로 감정과 성향을 분석하여 AI가 영화를 추천합니다</p>
                                </div>
                                <img src="@/assets/tutorials/tutorial6.png" class="d-block w-100 howtoimg" alt="6">
                            </div>
                            <div class="carousel-item carousel-item-htp">
                                <div>
                                    <h2 class="explanation-title-htp">7. 댓글 남기기</h2>
                                    <p class="explanation-context-htp">플레이한 영화의 후기를 댓글로 남길 수 있습니다</p>
                                </div>
                                <img src="@/assets/tutorials/tutorial7.png" class="d-block w-100 howtoimg" alt="7">
                            </div>
                            <div class="carousel-item carousel-item-htp">
                                <div>
                                    <h2 class="explanation-title-htp">8. 전적 검색</h2>
                                    <p class="explanation-context-htp">플레이한 영화의 결과를 다시 볼 수 있습니다</p>
                                </div>
                                <img src="@/assets/tutorials/tutorial8.png" class="d-block w-100 howtoimg" alt="8">
                            </div>
                            <div class="carousel-item carousel-item-htp">
                                <div>
                                    <h2 class="explanation-title-htp">9. 영화 제작</h2>
                                    <p class="explanation-context-htp">자신만의 영화도 만들 수 있습니다</p>
                                </div>
                                <img src="@/assets/tutorials/tutorial9.png" class="d-block w-100 howtoimg" alt="9">
                            </div>
                        </div>
                    </div>
                </div>
                <div class="modal-footer modal-footer-htp">
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions"
                        data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                    </button>
                    <div class="carousel-indicators">
                        <button v-for="(_, index) in 9" :key="index" type="button"
                            :class="['indicator-btn', { active: currentSlide === index }]"
                            @click="setCurrentSlide(index)" :aria-label="`Slide ${index + 1}`"></button>
                    </div>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions"
                        data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const currentSlide = ref(0);

const setCurrentSlide = (index) => {
    currentSlide.value = index;
};

onMounted(() => {
    const carousel = document.getElementById('carouselExampleCaptions');
    carousel.addEventListener('slide.bs.carousel', (event) => {
        currentSlide.value = event.to;
    });
});
</script>

<style scoped>
body {
    margin: 0
}

.carousel-item-htp {
    /* display: flex; */
}

.modal-content.modal-content-htp {
    background-color: var(--black06);
    border-color: var(--black15)
}

.modal-header.modal-header-htp,
.modal-body.modal-body-htp,
.modal-footer.modal-footer-htp {
    border: 1px solid var(--black15);
    text-align: center;
}

.btn-close.btn-close-htp {
    filter: invert(1);
}

.modal-body.modal-body-htp.modal-body-htp-text,
.modal-body.modal-body-htp.modal-body-htp-images {
    text-align: center;
}

.modal-footer.modal-footer-htp {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0.5rem;
    gap: 1rem;
}

.carousel-control-prev,
.carousel-control-next {
    position: static;
    width: auto;
    padding: 0.5rem;
}


.carousel-indicators {
    position: static;
    margin: 0;
    justify-content: center;
}

.explanation-context-htp {
    color: var(--grey60);
}

.indicator-btn {
    width: 30px;
    height: 4px;
    border-radius: 0;
    background-color: #FFFFFF;
    border: none;
    margin: 0 5px;
    transition: background-color 0.3s ease;
}

.indicator-btn.active {
    background-color: var(--red45);
}

.btn.btn-secondary.close-btn-htp {
    background-color: var(--black15);
    border: 2px solid var(--grey60);
    width: 60px;
}

.btn.btn-secondary.close-btn-htp:hover {
    background-color: var(--grey60);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.btn.btn-secondary {
    background-color: var(--black15);
    border: 2px solid var(--red45);
    transition: all 0.3s ease;
    width: 300px;
    height: 40px;
    text-align: center;
    font-size: larger;
}

.btn.btn-secondary:hover {
    background-color: var(--red45);
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(131, 2, 19, 0.4);
}

.howtoimg {
    /* width: 30rem;
    height: 40rem; */
    width: 50vw;
    height: 50vh;
    border: 2px solid var(--black15);
}
</style>