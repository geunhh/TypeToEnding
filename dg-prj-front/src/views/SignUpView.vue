<template>
    <div>
        <!-- No Longer Used!!! Deprecated!!! -->
        <!-- No Longer Used!!! Deprecated!!! -->
        <!-- No Longer Used!!! Deprecated!!! -->
        <!-- No Longer Used!!! Deprecated!!! -->
        <!-- No Longer Used!!! Deprecated!!! -->
        <!-- No Longer Used!!! Deprecated!!! -->
        <!-- No Longer Used!!! Deprecated!!! -->
        <!-- No Longer Used!!! Deprecated!!! -->
        <!-- No Longer Used!!! Deprecated!!! -->
        <!-- No Longer Used!!! Deprecated!!! -->
        <!-- No Longer Used!!! Deprecated!!! -->
        <!-- No Longer Used!!! Deprecated!!! -->
        <!-- No Longer Used!!! Deprecated!!! -->
        <!-- No Longer Used!!! Deprecated!!! -->
        <!-- No Longer Used!!! Deprecated!!! -->
        <!-- No Longer Used!!! Deprecated!!! -->
        <!-- No Longer Used!!! Deprecated!!! -->
        <!-- No Longer Used!!! Deprecated!!! -->
        <!-- No Longer Used!!! Deprecated!!! -->
        <!-- No Longer Used!!! Deprecated!!! -->
        <h1>회원가입</h1>
        <div style="text-align: left; margin-left: 10%;">
        <form @submit.prevent="signUp">
            <label for="email">email : </label>
            <input type="text" id="email" v-model.trim="email"><br>
            
            <label for="password1">password : </label>
            <input type="text" id="password1" v-model.trim="password1"><br>
            
            <label for="password2">confirm_password : </label>
            <input type="text" id="password2" v-model.trim="password2"><br>

            <!-- 회원 가입시 닉네임 입력도 추가 -->
            <label for="name">name : </label>
            <input type="text" id="name" v-model.trim="name"><br>

            <input type="submit" value="회원가입">
        </form>
        </div>
    </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/accountStore';
import { ref } from 'vue';
const store = useAccountStore()

const email = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const name = ref(null)

// 닉네임 필드 추가
const signUp = function () {
    const payload = {
        email : email.value,
        password1 : password1.value,
        password2 : password2.value,
        name : name.value,
    }
    store.signUp(payload)
}

</script>

<style scoped>


</style>