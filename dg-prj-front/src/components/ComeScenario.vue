<template>
    <div>
        <h1>시나리오 생성중...</h1>
        <p>지금은 3초 뒤에 게임페이지로 넘어가는데, 나중에 최소 3초 + 데이터 넘어오면 가기</p>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { onMounted } from 'vue';
import { useGameStore, useMovieStore } from '@/stores/counter';

const moviestore = useMovieStore()
const router = useRouter()
const gamestore = useGameStore()
onMounted(() => {
    // 3초 후에 이동
    gamestore.getInitial()
    setTimeout(() => {
        router.push({name:'GamePlayView', params: { roomId : moviestore.roomId}})  
  }, 3000);
})

 

</script>

<style lang="scss" scoped>

</style>