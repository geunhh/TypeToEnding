<template>

  <div>
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
import { RouterLink, RouterView } from 'vue-router';

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

<style>
.music-button {
  position: absolute;
  /* 위치는 인게임 테스트를 거치면서 기깔나게 좀 바꿔보자 */
  top: 200px;
  left: 200px;
  padding: 10px 20px;
  font-size: 16px;
  background: transparent;
  border: 0px;
  z-index: 1000;
}

.music-button-icon {
  width: 80px;
  height: 80px;
}
</style>