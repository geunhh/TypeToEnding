<template>
    <div>
        <h1> Round : {{ gamestore.game_round }}</h1>
        <div class="playgame-container">
        <!-- <p>{{ moviestore.movie_name }}</p>
        <p>{{ moviestore.description }}</p> -->
        <!-- 상단 bar -->
        <div class="high-bar">
            구현 예정 
        </div>
        <div class="description-game"> 주어진 상황에 이어질 시나리오를 작성하시오</div>
        <div class="scenario-container">
            <div class="scenario-box">시나리오 설명창
                <p>{{ gamestore.initial_question      }}</p>
            </div>

            <div class="prompt-box">시나리오 작성창 
                <textarea name="" id="" style="width: 100%; height: 90%;"
                            v-model="useraction">
                </textarea>
            </div>
            
        </div>
        <button class="submit-btn" @click="goEval">
        시나리오 제출 {{ gamestore.game_id }}
    </button>

    </div>
</div>
</template>

<script setup>
import { useGameStore, useMovieStore, useUserStore } from '@/stores/counter';
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter()
const useraction = ref(null)
const moviestore = useMovieStore()
const gamestore = useGameStore()
const userstore = useUserStore()

const goEval = function () {
    gamestore.user_action1 = useraction.value    
    router.push({name: 'evaluation'})   
    
    
}


</script>

<style scoped>
.submit-btn{
    padding: 10px 20px;
    font-size: large;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    color: white;
    background-color:red;
}
.playgame-container{
    margin: 20px;
}
.high-bar{
    border: 1px gray solid;
    border-radius: 10px;
    background-color: black;
    color: white;
}
.description-game{
    
    border: 1px gray solid;
    border-radius: 10px;
    background-color: black;
    color: white;
    width: fit-content;
    margin: 20px auto;
    padding: 5px 50px;
}
.scenario-container {
  display: flex;
  justify-content: center; /* 수평 중앙 정렬 */
  align-items: center;     /* 수직 중앙 정렬 */
  gap: 20%;               /* 픽셀 단위로 큰 간격 설정 */
  margin-top: 40px;        /* 추가 여백 */
}
.scenario-box, .prompt-box {
  padding: 20px;
  font-size: medium;
  border-radius: 10px;
  background-color: black;
  color: white;
  width: 400px;
  height: 500px;
  text-align: center; /* 내부 텍스트를 가운데 정렬 */
}
.prompt-box {
  background-color: gray; /* prompt-box만 다른 배경색으로 설정 */
}
</style>