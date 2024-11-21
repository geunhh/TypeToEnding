<template>
    <div style="margin: 100px; ">
        
        <h1>최종 결과 페이지</h1>
        <hr>
        <button @click="recommend_toggle" :disabled="!recommend">영화 추천 받기 토글</button><br>
        <div v-if="isRecommend">
            {{ recommend_info.results[0].poster_path }}
            <h3> 스토리 요약</h3>
            <p> {{ recommend.story_summary }}</p><hr>
            <h3>감정 분석</h3>
            <p>{{ recommend.psychological_analysis }}</p><hr>
            <h3>영화 추천</h3>
            <img :src="`https://image.tmdb.org/t/p/w400${recommend_info.results[0].poster_path}`" alt="추천 영화 포스터">
            <!-- <img :src="`https://image.tmdb.org/t/p/w$400/z7ilT5rNN9kDo8JZmgyhM6ej2xv.jpg/`" alt=""> -->
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
const recommend_info = ref(null)



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
    .then(res =>{
        // 추천 받은 영화 정보를 받아와야 함. 그래서 TMDB에 axios 보낼거임.
        axios({
            method:'get',
            url: `https://api.themoviedb.org/3/search/movie`,
            headers: {
                accept: 'application/json',
                Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNmFmOGIwNGUyZTI0MTgwZGQ5NTgxMTFhOWIwMzVkOCIsIm5iZiI6MTczMjE3NDI2Ny45MTU4ODEsInN1YiI6IjY3MjEwNWE2NGJlMTU0NjllNzBlNzhkMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Hn679BEcxrEDiQhMZmHkI0oJlM93CpNmgDVxNlUwBWM'
            },
            params:{
                include_adult:true,
                language:"ko-KR",
                page:1,
                query: recommend.value.recommended_movie.title,
            }
        }).then(res =>{
            console.log('ggg',res)
            recommend_info.value = res.data

        })
    })})
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