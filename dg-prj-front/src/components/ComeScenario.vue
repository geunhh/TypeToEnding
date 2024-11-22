<template>
    <div class="bigbig-container">
        <h1 class="h1">시나리오 생성중...</h1>
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
    if (gamestore.game_round === 0) {
        gamestore.getInitial()
        setTimeout(() => {
            router.push({name:'GamePlayView', params: { roomId : moviestore.roomId}})  
        }, 2000);        
    }
    else {
        console.log(router)
        setTimeout(() => {
            router.push({name:'GamePlayView', params: { roomId : moviestore.roomId}, 
                        state: { next_problem:router.next_problem }})  
        }, 2000);
    }
            
    
})

 

</script>

<style scoped>
.bigbig-container{
  padding : 5rem;
  text-align: center;
}

</style>