<template>
    <div style="margin: 20%;">
        <h1>영화 생성 페이지</h1>
        <hr>
        <form @submit.prevent="submitFunc">
            <label for="">제목</label>
            <input type="text" v-model="new_title"><br>
            <label for="">줄거리</label>
            <textarea name="" id="" v-model="new_description"></textarea><br>
            <label for="">세계관</label>
            <textarea name="" id="" v-model="new_context"></textarea><br>
            <input type="submit">
        </form>
    </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/accountStore';
import axios from 'axios';
import { ref } from 'vue';

const new_title = ref(null)
const new_description = ref(null)
const new_context = ref(null)
const accountstore = useAccountStore()

const submitFunc = function () {
    
    axios({
        method : 'post',
        url : 'http://127.0.0.1:8000/gameApp/movielist/',
        headers: {
            Authorization: `Token ${accountstore.token}`
        },
        data : {
            title : new_title.value,
            description : new_description.value,
            context : new_context.value,
            creator : accountstore.userId
        }
        
     }).then((res) => console.log(res))
     .catch(err=>console.log(err))
    
}

</script>

<style lang="scss" scoped>

</style>