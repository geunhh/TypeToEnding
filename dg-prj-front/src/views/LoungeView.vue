<template>
    <div class="bigbig-container">
        <!-- 헤더 섹션 -->
        <div class="header-section" style="position: relative; text-align: center;">
            <div class="back-icon" @click="gohome">
                <i style="font-size: 4.5rem;color: #830213; " class="bi bi-house-fill"></i>

            </div>
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
                <div class="poster-wrapper">
                    <img class="poster" :src="`http://127.0.0.1:8000${moviestore.poster_path}`"
                        v-if="moviestore.poster_path">
                    <img class="poster" src='@/assets/selectimg.jpeg' v-else>
                </div>
                <button class="btn-select" @click="gogoSelect">
                    <i class="bi bi-film"></i> 영화 선택
                </button>
            </div>

            <!-- 설명 섹션 -->
            <div class="description-section">
                <div class="description-box">
                    <p v-if="moviestore.movieId">{{ moviestore.description }}</p>
                    <p v-else>영화 줄거리가 들어갈 공간입니다.</p>
                </div>
                <button class="btn-start" @click="startGame" :disabled="moviestore.movieId == null"
                    :class="{ 'active': moviestore.movieId }">
                    게임 시작
                </button>
            </div>

            <!-- 정보 섹션 -->
            <div class="info-section">
                <div class="howtoplay">
                    HOW TO PLAY
                </div>

                <div class="cast-info">
                    <h3>Cast Info</h3>
                    <div class="cast-list">
                        <div class="cast-item">
                            <span class="cast-role">주인공</span>
                            <span class="cast-player" style="font-size: large;"> {{ store.userInfo.name }}</span>
                        </div>
                        <div class="cast-item">
                            <span class="cast-role">조연 1</span>
                            <span class="cast-player">player X</span>
                        </div>
                        <div class="cast-item">
                            <span class="cast-role">조연 2</span>
                            <span class="cast-player">player X</span>
                        </div>
                        <div class="cast-item">
                            <span class="cast-role">조연 3</span>
                            <span class="cast-player">player X</span>
                        </div>
                        <div class="cast-item">
                            <span class="cast-role">조연 4</span>
                            <span class="cast-player">player X</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/accountStore';
import { useMovieStore, useUserStore } from '@/stores/counter';
import { useRouter } from 'vue-router';
const router = useRouter()
const store = useAccountStore()
const moviestore = useMovieStore()

const gogoSelect = function () {
    router.push({ name: 'SelectMovie' })
}

const startGame = function () {
    console.log('게임을 시작합니다.')
    router.push({ name: 'loading' })
}

const gohome = function () {
    router.push({ name: 'main' })
}


</script>

<style scoped>
.back-icon {
    position: absolute;
    left: 5rem;
    top: 50%;
    transform: translateY(-50%);
    cursor: pointer;
    transition: all 0.3s ease;
}

.bigbig-container {
    padding: 5rem 10rem;
    background-color: #1A1A1A;
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
    text-shadow: 0px 4px 4px #00000040;
}

.theater-code {
    background-color: #830213;
    display: inline-flex;
    padding: 0.8rem 1.5rem;
    border-radius: 8px;
    gap: 1rem;
}

.code-label {
    color: rgba(255, 255, 255, 0.8);
    font-size: 0.9rem;
}

.code-value {
    color: #ffffff;
    font-weight: 600;
    letter-spacing: 2px;
}

/* 그리드 레이아웃 */
.grid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
    margin-top: 2rem;
}

/* 포스터 섹션 */
.poster-wrapper {
    margin-bottom: 1.5rem;
}

.poster {
    width: 70%;
    border-radius: 12px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
    transition: transform 0.3s ease;
}

.poster:hover {
    transform: translateY(-5px);
}

.btn-select {
    background-color: #830213;
    color: white;
    padding: 0.8rem 1.5rem;
    border: none;
    border-radius: 8px;
    font-weight: 500;
    transition: all 0.3s ease;
}

.btn-select:hover {
    background-color: #9f0217;
    transform: translateY(-2px);
}

/* 설명 섹션 */
.description-box {
    background-color: #2d2d2d;
    padding: 2rem;
    border-radius: 12px;
    height: 90%;
    margin-bottom: 1.5rem;
    color: #ffffff;
    line-height: 1.6;
}

.btn-start {
    background-color: #8B8680;
    color: white;
    padding: 1rem 2rem;
    border: none;
    border-radius: 8px;
    font-size: 1.1rem;
    font-weight: 500;
    transition: all 0.3s ease;
}

.btn-start.active {
    background-color: #830213;
}

.btn-start.active:hover {
    background-color: #9f0217;
    transform: translateY(-2px);
}

/* 정보 섹션 */
.howtoplay {
    background-color: #830213;
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
    background-color: #9f0217;
    transform: translateY(-2px);
}

.cast-info {
    background-color: #2d2d2d;
    padding: 2rem;
    border-radius: 12px;
    color: white;
}

.cast-info h3 {
    margin-bottom: 1.5rem;
    color: #830213;
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
        padding: 2rem;
    }

    .grid-container {
        grid-template-columns: 1fr;
    }

    .info-section {
        grid-column: span 1;
    }
}
</style>