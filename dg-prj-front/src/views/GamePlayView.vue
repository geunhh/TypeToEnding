<template>
    <div class="bigbig-container" >
        <!-- 상단 bar -->
        <div class="playgame-container container text-center">
        <div class="high-bar" :class="flex">
            <div class="row" style="display: flex; align-items: center; justify-content: center;">
                <div class="col-sm-2" >
                 <h1># {{ gamestore.game_round+1 }}</h1 style="font-size: larger;">
                </div>
                <div class="col-sm-7" style="text-align: left; 
                    border-right: 1px gray solid;
                    border-left: 1px gray solid ;
                    padding: 0 0;" 
                    >
                    <div class="col" style="border-bottom: 1px solid gray; padding: 0 5px;">
                        <h5>영화 : {{ moviestore.movie_name }}</h5>

                    </div>
                    <div class="col" style="padding: 0 5px; ">
                        <h5>감독 : {{ accountstore.userInfo.name }}</h5>
                    </div>
                </div>
                <div class="col-sm-3" style="padding-left: 0;">
                    <div class="row" style="border-bottom: 1px gray solid; margin: 0;">
                        <div class="col" style="border-right: 1px gray solid;font" >{{ month }} / {{ day }}</div>
                        <div class="col"></div>
                    </div>
                    <div class="row">
                        <div class="col-sm-6" style="text-align: center;">
                        <span style="color: red;">__</span>
                        <span :style="{ color: gamestore.game_round>0 ? 'red' : ''}">__</span>
                        <span :style="{ color: gamestore.game_round>1 ? 'red' : ''}">__</span>
                        <span :style="{ color: gamestore.game_round>2 ? 'red' : ''}">__</span>
                        <span :style="{ color: gamestore.game_round>3 ? 'red' : ''}">__</span>
                    </div>
                        
                        
                    </div>
                </div>

            </div>
        </div>
        <div class="description-game"><h4> 주어진 상황에 이어질 시나리오를 작성하시오</h4></div>
        <div class="scenario-container">
            <div class="scenario-box" style="font-size: larger;">
                <p>시나리오 설명창</p>
                <p v-if="gamestore.next_situation">{{ gamestore.next_situation }}</p> 
                <p v-else>{{ gamestore.initial_question }}</p> 
            </div>

            <div class="prompt-box">
                <p>시나리오 작성창 </p>
                <textarea style="width: 100%; height: 90%; background-color: darkgray;"
                            v-model="useraction">
                </textarea>
            </div>
            
        </div>
        <button class="submit-btn" @click="goEval" style="margin-top: 30px;">
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
let today = new Date()
let month = today.getMonth()+1
let day = today.getDate()




const goEval = function () {
    if (useraction.value.length < 11) {
        alert('시나리오가 너무 짧습니다.')
    }
    else {
    gamestore.user_action1 = useraction.value    
    router.push({name: 'evaluation'})   
    }
    
}


</script>

<style scoped>
.row span{
    padding: 0 2px;
}
.row svg{
    display: inline-block;
    padding: 0;
}
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