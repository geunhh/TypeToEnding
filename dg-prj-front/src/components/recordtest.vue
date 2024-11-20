<template>
    <div>

        <h1>test</h1>

    </div>
</template>

<script setup>
import { useUserStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted } from 'vue';
const userstore = useUserStore()

onMounted(() => {
axios({
    method : 'get',
    url:' http://127.0.0.1:8000/gameApp/test/',
    headers : {
        Authorization: `Token ${userstore.token}`
    },
}).then(res => console.log(res))
.catch(err => console.log(err))
})

</script>

<style scoped>

</style>