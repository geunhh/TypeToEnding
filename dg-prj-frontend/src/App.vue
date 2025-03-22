<template>

  <div>

    <button class="home-icon" @click.prevent="goHome">
      <i style="font-size: 3rem;color: var(--red45); " class="bi bi-house-fill"></i>
    </button>

    <button class="music-button" v-if="isPlaying">
      <img class="music-button-icon" src="@/assets/icons/music-on.png" alt="music-on" @click="toggleMusic">
    </button>
    <button class="music-button" v-else>
      <img class="music-button-icon" src="@/assets/icons/music-off.png" alt="music-off" @click="toggleMusic">
    </button>

    <RouterView />
  </div>
</template>


<script setup>
import { ref } from 'vue';
import { RouterLink, RouterView, useRouter } from 'vue-router';

const router = useRouter()

const goHome = () => {
  router.push({ name: 'main' })
}

const audioFiles = [
  new URL('@/musics/music1.mp3', import.meta.url).href,
  new URL('@/musics/music2.mp3', import.meta.url).href,
  new URL('@/musics/music3.mp3', import.meta.url).href
];

const audio = ref(null);
const isPlaying = ref(false);

// 랜덤 음악을 재생하는 함수
function playRandomMusic() {
  const randomIndex = Math.floor(Math.random() * audioFiles.length);
  audio.value = new Audio(audioFiles[randomIndex]);

  audio.value.loop = true; // 항상 반복 재생 설정
  audio.value.play().catch(error => {
    console.error("음악 재생 중 오류 발생:", error);
  });

  isPlaying.value = true;
}

// 음악을 켜고 끄는 함수
function toggleMusic() {
  if (isPlaying.value) {
    audio.value.pause();
    isPlaying.value = false;
  } else {
    playRandomMusic();
  }
}
</script>

<style scoped>
.home-icon {
  background-color: transparent;
  border: 0px;
  position: fixed;
  top: 2rem;
  right: 5rem;
  /* transform: translateY(-50%); */
  cursor: pointer;
  transition: all 0.3s ease;
}

.home-icon:hover {
  transform: translateY(-2px);
}

.music-button {
  position: fixed;
  top: 7rem;
  right: 5rem;
  background: linear-gradient(to right, #1A1A1A, #2d2d2d);
  border: 1px solid rgba(80, 0, 10, 0.3);
  /* 더 어두운 레드로 변경 */
  border-radius: 50%;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  padding: 0;
}

.music-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(80, 0, 10, 0.4);
  /* 그림자도 더 어둡게 */
  background: linear-gradient(to right, #500010, #6b0012);
  /* 더 어두운 그라데이션 */
}

.music-button img {
  width: 25px;
  height: 25px;
  filter: invert(5%) sepia(70%) saturate(4000%) hue-rotate(345deg) brightness(70%) contrast(101%);
  /* 더 어두운 필터 */
  transition: all 0.3s ease;
}

.music-button:hover img {
  filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(93deg) brightness(103%) contrast(103%);
}
</style>