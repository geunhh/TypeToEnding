<template>

    <div class="bigbig-container">
        <!-- 헤더 섹션 -->
        <video autoplay loop muted class="background-video" ref="backgroundVideo">
            <source src="@/assets/movies/background.mp4" type="video/mp4">
        </video>
        <div class="header-section" style="position: relative; text-align: center;">
            <!-- <button class="back-icon" @click="gohome">
                <i style="font-size: 3rem;color: var(--red45); " class="bi bi-house-fill"></i>
            </button> -->
            <h1 class="title">Type to Ending </h1>
            <div class="theater-code">
                <span class="code-label">Theater Code</span>
                <span class="code-value">{{ moviestore.roomId.slice(0, 4).toUpperCase() }}</span>
            </div>
        </div>

        <!-- 메인 그리드 -->
        <div class="grid-container">
            <!-- 포스터 섹션 -->
            <div class="poster-section" style="text-align: center;">
                <img class="poster" :src="`http://127.0.0.1:8000${moviestore.poster_path}`"
                    v-if="moviestore.poster_path" @click="gogoSelect">
                <img class="poster" src='@/assets/posters/movieNotSelected.png' v-else @click="gogoSelect">

            </div>

            <div class="sub-container">
                <!-- 설명 섹션 -->


                <div class="description-box" style="font-family: 'Gowun Dodum', serif; font-size: larger;">
                    <h1 style="margin-bottom: 20px;">영화 줄거리</h1>
                    <p v-if="moviestore.movieId">{{ moviestore.description }}</p>
                    <p v-else>영화 줄거리가 들어갈 공간입니다.</p>
                </div>

                <!-- 정보 섹션 -->
                <div class="info-section">
                    <!-- how to play modal -->
                    <div class="cast-info">
                        <h3>Cast Info</h3>
                        <div class="cast-list">
                            <div class="cast-item">
                                <span class="cast-role">주인공</span>
                                <span class="cast-player" style="font-size: large;"> {{ store.userInfo.name }}</span>
                            </div>
                            <div class="cast-item">
                                <span class="cast-role">조연 1</span>
                                <span class="cast-player">타락해버린 히로인</span>
                            </div>
                            <div class="cast-item">
                                <span class="cast-role">조연 2</span>
                                <span class="cast-player">개과천선한 마왕군 2인자</span>
                            </div>
                            <div class="cast-item">
                                <span class="cast-role">조연 3</span>
                                <span class="cast-player">모든 일의 원흉이었던 동료</span>
                            </div>
                        </div>
                    </div>

                    <div>
                        <howToPlay />
                    </div>
                    <button class="btn-select" @click="gogoSelect">
                        <i class="bi bi-film"></i> 영화 선택
                    </button>
                    <button class="btn-start" @click="startGame" :disabled="moviestore.movieId == null"
                        :class="{ 'active': moviestore.movieId }">
                        게임 시작
                    </button>
                </div>

            </div>
        </div>
    </div>
</template>

<script setup>
import howToPlay from '@/components/howToPlay.vue';
import { useAccountStore } from '@/stores/accountStore';
import { useMovieStore, useUserStore } from '@/stores/counter';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter()
const store = useAccountStore()
const moviestore = useMovieStore()
const backgroundVideo = ref(null);

onMounted(() => {
    // 재생 속도를 느리게 설정
    if (backgroundVideo.value) {
        backgroundVideo.value.playbackRate = 0.5; // 0.5배속으로 설정
    }
});
const gogoSelect = function () {
    router.push({ name: 'SelectMovie' })
}

const startGame = function () {
    // console.log('게임을 시작합니다.')
    router.push({ name: 'loading' })
}

const gohome = function () {
    router.push({ name: 'main' })
}


</script>

<style scoped>
.poster-section {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem 3rem 2rem 2rem; /* 위, 오른쪽, 아래, 왼쪽 순서 */
    border-right: 2px solid var(--black15);
    text-align: center;
}



.sub-container {
    display: flex;
    gap: 50px;
    /* justify-content: space-between; */
    width: 100%;
}


.background-video {
    position: fixed;
    right: 0;
    bottom: 0;
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
    z-index: -1;
    object-fit: cover;
}

.back-icon {
    background-color: transparent;
    border: 0px;
    position: fixed;
    top: 5rem;
    right: 5rem;
    transform: translateY(-50%);
    cursor: pointer;
    transition: all 0.3s ease;
}

.bigbig-container {
    padding: 5rem 27rem;
    /* background-color: var(--black10); */
    background-color: transparent;
    min-height: 100vh;
}

/* 헤더 스타일링 */
.header-section {
    margin-bottom: 4rem;
}

.title {
    align-self: center;
    color: var(--absolutewhite);
    font-family: var(--font-family-inknut_antiqua);
    font-size: var(--font-size-xxl);
    font-weight: 400;
    letter-spacing: 0;
    line-height: normal;
    text-shadow: 0px 4px 4px var(--black06);
}

.theater-code {
    background-color: var(--red45);
    display: inline-flex;
    padding: 0.8rem 1.5rem;
    border-radius: 8px;
    gap: 1rem;
    align-items: center;
    justify-content: center;
}

.code-label {
    color: rgba(255, 255, 255, 0.8);
    font-size: 2rem;
}

.code-value {
    color: #ffffff;
    font-weight: 600;
    letter-spacing: 2px;
    font-size: 2rem;
}

/* 그리드 레이아웃 */
.grid-container {
    border: 2px solid var(--black15);
    display: flex;
    border-radius: 8px;
    padding: 1rem;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
    margin-top: 2rem;
    height: 700px;
}

/* 포스터 섹션 */
.poster-wrapper {
    margin-bottom: 1.5rem;
}

.poster {
    border: 2px solid var(--abbey);
    border-radius: 12px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
    transition: transform 0.3s ease;
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
}

.poster:hover {
    transform: translateY(-5px);
}

.btn-select {
    background-color: var(--black10);
    color: white;
    padding: 0.8rem 1.5rem;
    border: 2px solid var(--red45);
    border-radius: 8px;
    font-weight: 500;
    transition: all 0.3s ease;
    height: 64px;
}

.btn-select:hover {
    background-color: var(--red45);
    transform: translateY(-2px);
}

/* 설명 섹션 */
.description-box {
    background-color: var(--black26);
    padding: 1rem;
    border-radius: 12px;
    color: #ffffff;
    line-height: 1.6;
    overflow-y: auto;
    width: 800px;
}

.btn-start {
    background-color: var(--grey60);
    color: white;
    padding: 1rem 2rem;
    border: none;
    border-radius: 8px;
    font-size: 1.1rem;
    font-weight: 500;
    transition: all 0.3s ease;
    height: 64px;
}

.btn-start.active {
    background-color: var(--black10);
    border: 2px solid var(--red45);
}

.btn-start.active:hover {
    background-color: var(--red45);
    transform: translateY(-2px);
}

/* 정보 섹션 */
.howtoplay {
    background-color: var(--red45);
    color: white;
    padding: 1rem 2rem;
    border-radius: 8px;
    font-weight: 600;
    display: inline-block;
    margin-bottom: 2rem;
    cursor: pointer;
    transition: all 0.3s ease;
}

.howtoplay:hover {
    background-color: var(--red45);
    transform: translateY(-2px);
}

.cast-info {
    background-color: var(--black26);
    padding: 1rem;
    border-radius: 12px;
    color: white;
}

.cast-info h3 {
    margin-bottom: 1.5rem;
    color: var(--red45);
}

.cast-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.cast-item {
    display: flex;
    justify-content: space-between;
    padding: 0.5rem 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.cast-role {
    color: rgba(255, 255, 255, 0.7);
}

.cast-player {
    color: #ffffff;
    font-weight: 500;
}

.info-section {
    display: flex;
    flex-direction: column;
    gap: 2rem;
    width: 344px;
}

/* 반응형 디자인 */
@media (max-width: 1200px) {
    .grid-container {
        grid-template-columns: 1fr 1fr;
    }

    .info-section {
        grid-column: span 2;
    }
}

@media (max-width: 768px) {
    .bigbig-container {
        padding: 1rem;
    }
    .grid-container {
        grid-template-columns: 1fr;
    }

    .info-section {
        grid-column: span 1;
    }
}
</style>