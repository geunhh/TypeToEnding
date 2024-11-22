<template>
    <div class="bigbig-container">
        <h1> Round : {{ gamestore.game_round+1 }}</h1>
        <!-- 상단 bar -->
        <div class="playgame-container container text-center">
        <div class="high-bar" :class="flex">
            <div class="row">
                <div class="col-sm-2" >
                 <h3># {{ gamestore.game_round+1 }}</h3>
                </div>
                <div class="col-sm-5" >
                    <div class="col">
                        <h2>영화 : {{ moviestore.movie_name }}</h2>
                    </div>
                    <div class="col">
                        <h2>감독 : {{ accountstore.userInfo.name }}</h2>
                    </div>
                </div>
                <div class="col-sm-3">
                    ggg
                </div>

            </div>
        </div>
        <div class="description-game"> 주어진 상황에 이어질 시나리오를 작성하시오</div>
        <div class="scenario-container">
            <div class="scenario-box">시나리오 설명창
                <p v-if="gamestore.next_situation">{{ gamestore.next_situation }}</p> 
                <p v-else>{{ gamestore.initial_question }}</p> 
                <!-- 이거 고쳐야 함 -->
            </div>

            <div class="prompt-box">시나리오 작성창 
                <textarea name="" id="" style="width: 100%; height: 90%; background-color: darkgray;"
                            v-model="useraction">
                </textarea>
            </div>
            
        </div>
        <button class="submit-btn" @click="goEval">
        시나리오 제출 
    </button>

    </div>
</div>
</template>

<script setup>
import { useAccountStore } from '@/stores/accountStore';
import { useGameStore, useMovieStore, useUserStore } from '@/stores/counter';
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter()
const useraction = ref(null)
const moviestore = useMovieStore()
const gamestore = useGameStore()
const userstore = useUserStore()
const accountstore = useAccountStore()

const goEval = function () {
    gamestore.user_action1 = useraction.value    
    router.push({name: 'evaluation'})   
    
    
}


</script>

<style scoped>
.bigbig-container{
  padding : 5rem;
  text-align: center;
}
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