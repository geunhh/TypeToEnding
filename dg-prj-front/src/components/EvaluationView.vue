<template>
    <div>
        <h1 v-if="!isComplete">AI가 당신의 시나리오를 평가하는 중 입니다.</h1>
        <div v-else>
        <h1>평가가 끝났습니다!!</h1>
        <button @click="gonextStage">확인하기</button>
        </div>
        {{ gamestore.user_action1 }}
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { onMounted, ref } from 'vue';
import { useGameStore, useMovieStore, useUserStore } from '@/stores/counter';
import axios from 'axios';

const isComplete = ref(false)
const moviestore = useMovieStore()
const userstore = useUserStore()
const router = useRouter()
const gamestore = useGameStore()
// const gonextStage = function () {
//     router.push({
//         name:'roundresult',
//         state : {result :res.data},
//     })

// }
    
onMounted(() => {
    // 3초 후에 이동
    axios({
      method:'post',
      url:`http://127.0.0.1:8000/gameApp/play_game/${gamestore.game_id}/`,
      headers : {
        Authorization: `Token ${userstore.token}`
      },
      data: {
        user_action : gamestore.user_action1,
      } // 선택된 영화 ID를 이 변수에 담아 전송}
    })
    .then(res => {
      console.log(res)
      isComplete.value = true
      console.log(res.data)
      router.push({
        name: 'roundresult',
        state: { result: res.data }, // 데이터 상태로 전달
    });



    })
    .catch(err => {
      console.log(err)
    })
    
})
</script>

<style lang="scss" scoped>

</style>