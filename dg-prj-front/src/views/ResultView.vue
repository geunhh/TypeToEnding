<template>
    <div style="margin: 100px; ">
        
        <h1>최종 결과 페이지</h1>
        <hr>
        <button @click="recommend_toggle" :disabled="!recommend">영화 추천 받기 토글</button><br>
        <div v-if="isRecommend">
            <p> 스토리 요약</p>
            <p> {{ recommend.story_summary }}</p><hr>
            <h2>감정 분석</h2>
            <p>{{ recommend.psychological_analysis }}</p><hr>
            <h2>영화 추천</h2>
            <p>제목 : {{ recommend.recommended_movie.title }}</p>
            <p>추천 이유 : {{ recommend.recommended_movie.reason }}</p>
            <p>테마 : {{ recommend.recommended_movie.theme }}</p>
            
        </div>

          <!-- <p>{{ result }}</p> -->
        <div v-if="!result">로딩 중 입니다..</div>
        <div v-for="(res, index) in result.history" v-else style="text-align: left; font-size: smaller;" >
            <div v-if="index>0" class="result-content">
            <p>{{ index }}번 라운드</p>
            <p>상황 : {{ res.situation }}</p>
            <p>내 답변 : {{ res.user_action }}</p>

            <p>평가 : {{ res.evaluation }}</p>
            <p>{{ res.reason }}</p>
            <p>결과 : {{ res.next_situation }}</p>
            </div>
            <!-- <p>{{ res.situation }}</p> -->
            <hr>
        </div>
    </div>
</template>

<script setup>
import { useGameStore, useUserStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted, ref } from 'vue';
const result = ref()
const gamestore = useGameStore()
const userstore= useUserStore()
const isRecommend = ref(false)
const recommend = ref(null)



const recommend_toggle = function () {
    isRecommend.value = !isRecommend.value
    console.log(result.value)

        
}

onMounted(() => {
    console.log('gamenum:' ,gamestore.game_id)
    axios({
        method:'get',
        url:`http://127.0.0.1:8000/gameApp/record/${gamestore.game_id}/`,
        headers : {
            Authorization: `Token ${userstore.token}`,

        }
    })
    .then(res => {
        console.log(res.data); // 이러면 JSON 문자열 그대로 반환됨. 
        result.value = res.data; 

        // history가 JSON 문자열인 경우 파싱
        if (typeof res.data.history === 'string') {
            res.data.history = JSON.parse(res.data.history); // 그래서 파싱 해줌.
        }
        // result.value = res.data; 
    }).then(res=> {
        // 영화 추천 및 감정분석을 위한 axios 호출.
        axios({
            method:'post',
            url:`http://127.0.0.1:8000/gameApp/recommend/${gamestore.game_id}/`,
            headers : {
                Authorization: `Token ${userstore.token}`,
                "Content-Type": "application/json"
            },
            data : {
                result : result.value
            }
        }).then(res => {
            console.log(res)
            recommend.value = res.data.result
        })
    }).then({
        // 추천 받은 영화 정보를 받아와야 함. 그래서 TMDB에 axios 보낼거임.
    })
    .catch(err=> console.log(err))
})

</script>

<style scoped>
.result-content{
    font-size: smaller;
}
p {
    font-size: smaller;
}
</style>