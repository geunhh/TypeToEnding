<template>
    <div>
        <h1>Type to Ending</h1>
    </div>
    <div style="display: flex; justify-content: space-between;">
        <!-- not 로그인 창 -->
        <div class="login-container" v-if="!store.token">
            <form @submit.prevent="loginFunc">
                <label for="id">ID</label><br>
                <input type="text" v-model="email"><br>
                <label for="pw">Password</label><br>
                <input type="password" v-model="password"><br>
                <input type="submit" value="로그인">
            </form>                
            <button>
            <RouterLink :to="{name:'SignUpView'}">회원가입</RouterLink>     </button>
            {{ store.token }}
        </div>
        <!-- 로그인 창 -->
        <div class="login-container" v-else>
            <button class="afterlogin-btn" @click="console.log(store.userId)">Profile</button>
            <button class="afterlogin-btn" @click="CreateRoom">Create Room</button>
            <button class="afterlogin-btn">Enter Room</button>
            <br>
            <br>
            <button class="afterlogin-btn" style="background-color: gray;">Log Out</button>
            <button class="afterlogin-btn" style="background-color: gray;">Sign Out</button>

            {{ store.token }}
        </div>

        <div class="howtoplay-container" @click="testFunc">
            how to play
        </div>
    </div>
</template>

<script setup>
import { useUserStore } from '@/stores/counter';
import { ref } from 'vue';
import { RouterLink, useRouter } from 'vue-router';

import {v4 as uuidv4} from 'uuid'
const email = ref(null)
const password = ref(null)
const store = useUserStore()

const router = useRouter()

const testFunc = function () {
    console.log(email.value)    
    console.log(password.value)    
}

const loginFunc = function () {
    console.log(email.value)    
    console.log(password.value)    
    const payload = {
        email : email.value,
        password : password.value,
    }
    store.logIn(payload)
}

const CreateRoom = function () {
    // 방 번호가 랜덤으로 들어가야함. 이지만 나중에 해보자잇.

    const roomId = uuidv4()
    router.push({name:'LoungeView', params: {roomId}})
    
    
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

</style>