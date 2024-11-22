<template>
    <div class="bigbig-container">
    <div >
        <h1 class="title">Type to Ending</h1>
        <div class="theater-code" style="margin-top: -30px;">Theater Code : {{moviestore.roomId.slice(0,4).toUpperCase()}} </div>
        <!-- 일단 방코드는 roomID 앞 4글자 땄어. -->

    </div>
    <div class="grid-container">
        <div>
            <!-- <img class="poster" :src="store.movieId ? require('@/assets/selectimg.jpeg') : require('@/assets/defaultimg.jpeg')" alt=""><br> -->
            <img class="poster" :src="`http://127.0.0.1:8000${moviestore.poster_path}`" v-if="moviestore.poster_path">
            <img class="poster" src='@/assets/selectimg.jpeg' v-else><br>
            <button style="margin-top: 10px; font-weight: 500;" type="button" class="btn btn-danger" @click="gogoSelect">영화 선택</button>

        </div>
        
        <div>
            <div class="description" style="padding: 10px;">
                <p style="font-size: medium; padding: 5px;" v-if="moviestore.movieId">{{moviestore.description}}</p>
                <p style="font-size: medium;" v-else>영화 줄거리가 들어갈 공간입니다.</p>
            </div>
            <button class="start-game" @click="startGame" :disabled="moviestore.movieId==null"
                    :class="{ 'red-background': moviestore.movieId }">
        게임 시작
    </button>

        </div>
        <div>
            <div class="howtoplay-container" @click="testFunc">
                how to play
            </div>

            <div><h3>Cast Info</h3>
            <p>주인공 : player {{ store.userId }}</p>
            <p>조연1 : player X</p>
            <p>조연2 : player X</p>

            </div>

        </div>
    </div>
</div>
</template>

<script setup>
import { useMovieStore, useUserStore } from '@/stores/counter';
import { useRouter } from 'vue-router';
const router = useRouter()
const store = useUserStore()
const moviestore = useMovieStore()

const gogoSelect = function(){
    router.push({name:'SelectMovie'})
}

const startGame = function () {
    console.log('게임을 시작합니다.')
    router.push({name:'loading'})   
}



</script>

<style scoped>
.bigbig-container{
  padding : 5rem;
  text-align: center;
}
.title {
    align-self: center;
    color: var(--absolutewhite);
    font-family: var(--font-family-inknut_antiqua);
    font-size: var(--font-size-xxl);
    font-weight: 400;
    letter-spacing: 0;
    line-height: normal;
    margin-top: 87px;
    min-height: 248px;
    min-width: 816px;
    text-shadow: 0px 4px 4px #00000040;
}
.theater-code {
    background-color: black;
    width: 30%;
    padding: 10px;
    margin: auto;
}
.grid-container {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap:10px
}
.howtoplay-container {
    border-radius: 10px;
    background-color: red;
    font-weight: 600;
    font-size: x-large;
    padding: 10px;
    height: fit-content;
    width: fit-content;
    margin-top: 5%;
    margin-left: 50%;
    margin-bottom: 50px;
}
.poster{
    width: 70%;
    margin-top: 30px;
    border-radius: 20px;
    border: 1px white solid;
}
.select-movie{
    color: white;
    background-color: red;
    padding: 5px 10px;
    font-size: large;
}
.description{
    margin-top: 20px;
    background-color: black;
    height: 85%;
}
.red-background {
    background-color: red;
    color: white; /* 버튼 글씨 색을 흰색으로 변경 */
}
.start-game {
    padding: 10px 20px;
    font-size: large;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
.red-background{
    padding: 10px 20px;
    font-size: large;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    color: white;
    background-color:red;
}
</style>