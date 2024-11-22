<template>
    <div class="bigbig-container">
        <h1> Round : {{ gamestore.game_round }}</h1>
        <div class="playgame-container">
        <!-- <p>{{ moviestore.movie_name }}</p>
        <p>{{ moviestore.description }}</p> -->
        <!-- 상단 bar -->
        <div class="high-bar">
            구현 예정 
        </div>
        <div class="description-game"> 시나리오를 
            <span v-if="result.is_valid" style="color: blue; font-weight: 800;">채택</span>
            <span v-else style="color: red; font-weight: 800;">폐기</span>합니다. </div>
        <div class="scenario-container">
            <div class="scenario-box">유저 시나리오
                <p>{{   gamestore.user_action1 }}</p>
            </div>

            <div class="prompt-box"> 평가 결과
                <p>{{ result.reason }}</p>

                <p> </p>
            </div>
            
        </div>
        <div class="d-flex justify-content-end">
        <button type="button" class="btn btn-danger" @click="nextStage"
            style="margin-top: 15px;">
            <span v-if="gamestore.game_round==4">결말보기</span>
            <span v-else>다음으로</span>
        </button>
    </div>

    </div>
</div>
</template>

<script setup>
import ComeScenario from '@/components/ComeScenario.vue';
import { useGameStore, useMovieStore, useUserStore } from '@/stores/counter';
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter()
const useraction = ref(null)
const moviestore = useMovieStore()
const gamestore = useGameStore()

const result = ref(router.options.history.state.result)
const nextStage = function () {
    gamestore.game_round ++;
    if (gamestore.game_round > 4) {
        router.push({ name: 'ResultPage' }); // 여기에 결과 페이지의 라우트 이름을 사용하세요.
    }
    else {
        // game round 번째 시나리오가 오는 중입니다.
        router.push({name:'loading', query:{next_problem : result.value.next_problem}})

    }
    // 여기에 넣을겨
}




</script>

<style scoped>
.bigbig-container{
  padding : 5rem;
  text-align: center;
}
.btn-loc{
    margin-left: 10%;
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