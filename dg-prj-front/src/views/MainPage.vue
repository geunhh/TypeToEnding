<template>
    <!-- 게임 플레이 설명해주는 모달 -->
    <!--how to play modal-->
    <!--이녀석이 존재하는 페이지 : 메인페이지, 대기실-->
    <div class="black-bg show-how-to-play" v-if="isHowToPlayModalOpen" @click="closeHowToPlayModal">
        <howToPlay />
    </div>
    <!-- title -->
    <div>
        <h1>Type to Ending</h1>
    </div>

    <div style="display: flex; justify-content: space-between;">

        <!-- 로그인 이전 창 -->
        <!-- <div class="login-container" v-if="!store.token"> -->
        <div class="login-container" v-if="!accountStore.token">
            <form @submit.prevent="loginFunc">
                <label for="id">ID</label><br>
                <input type="text" v-model="email"><br>
                <label for="pw">Password</label><br>
                <input type="password" v-model="password"><br>
                <input type="submit" value="로그인">
            </form>
            <button>
                <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink>
            </button>
        </div>

        <!-- 로그인 이후 창 -->
        <div class="login-container" v-else>
            <!-- 프로필 페이지로 이동하는 버튼 -->
            <button class="afterlogin-btn" @click="moveToProfilePage">Profile</button>
            <!-- 방 생성 버튼 -->
            <button class="afterlogin-btn" @click="CreateRoom">Create Room</button>
            <!-- 방 입장 버튼 -->
            <button class="afterlogin-btn" @click="isEnterRoomModalOpen = true">Enter Room</button>
            <br>
            <br>
            <button class="afterlogin-btn" style="background-color: gray" @click.prevent="logOutFunc">Log Out</button>
        </div>

        <!-- 이 버튼 누르면 게임 설명 모달 띄워짐 -->
        <button class="howtoplay-container show-how-to-play" @click="howToPlayHandler">
            how to play
        </button>
    </div>
</template>

<script setup>
import howToPlay from '@/components/howToPlay.vue';
import { useAccountStore } from '@/stores/accountStore';
import { useMovieStore, useUserStore } from '@/stores/counter';
import { ref, onMounted } from 'vue';
import { RouterLink, useRouter } from 'vue-router';

import { v4 as uuidv4 } from 'uuid'
const email = ref(null)
const password = ref(null)
const store = useUserStore()
const moviestore = useMovieStore()
const router = useRouter()
const accountStore = useAccountStore()


const isEnterRoomModalOpen = ref(false);
const isHowToPlayModalOpen = ref(false);

onMounted(() => {
    moviestore.movie_name = null
    moviestore.description = null
    moviestore.context = null
    moviestore.poster_path = null
    moviestore.movieId = null

})

// 프로필 페이지로 이동하는 함수
const moveToProfilePage = () => {
    console.log(accountStore.userId)
    router.push({
        name: 'ProfilePageView',
        params: { userId: accountStore.userId }
    })
}

const testFunc = function () {
    console.log(email.value)
    console.log(password.value)
}

// 로그아웃 함수
const logOutFunc = function () {
    // console.log('button clicked!!!')
    accountStore.logOut()
}

// 로그인 함수
const loginFunc = function () {
    console.log(email.value)
    console.log(password.value)
    const payload = {
        email: email.value,
        password: password.value,
    }
    accountStore.logIn(payload)
}

const CreateRoom = function () {
    // 방 번호가 랜덤으로 들어가야함. 이지만 나중에 해보자잇.

    const roomId = uuidv4()
    moviestore.roomId = roomId
    console.log(moviestore.roomId)
    router.push({ name: 'LoungeView', params: { roomId } })
}



const closeEnterRoomModal = (event) => {
    if (event.target.classList.contains('room-enter')) {
        isEnterRoomModalOpen.value = false;
    }
}

// 게임 설명 모달을 닫아주는 함수 >> 모달 외부 클릭하면 닫아짐
const closeHowToPlayModal = (event) => {
    if (event.target.classList.contains('show-how-to-play')) {
        isHowToPlayModalOpen.value = false;
    }

}
// 게임 설명 모달을 열어주는 함수
const howToPlayHandler = (event) => {
    // console.log("good@!");
    isHowToPlayModalOpen.value = true
}

// const enterRoomFunc = () => {
//     console.log(roomCode.value)
// }

// 대기실로 입장하는 함수
const moveToWaitingRoom = () => {
    router.push({
        name: 'WaitingRoomView',
        params: { roomCode: "3F7D" }
    })
}


</script>

<style scoped>
.login-container {
    border: 1px gray solid;
    border-radius: 5%;
    width: 30%;
    text-align: left;
    padding-left: 10px;
    margin-top: 5%;
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 15px;


}

.howtoplay-container {
    border: 1px white solid;
    background-color: red;
    font-weight: 600;
    padding: 10px;
    height: fit-content;
    margin-top: 5%;

}

.afterlogin-btn {
    width: 85%;
    color: white;
    background-color: red;
    font-size: x-large;
    border-radius: 15px;
    margin-top: 30px;
}

body {
    margin: 0
}

div {
    box-sizing: border-box;
}

.black-bg {
    width: 100%;
    height: 100%;
    background: #1e1e1e;
    position: fixed;
    padding: 20px;
}

.white-bg {
    color: #000000;
    width: 100%;
    background: #FFFFFF;
    border-radius: 8px;
    padding: 20px;
}
</style>