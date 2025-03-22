<template>
    <div>

        <h1>test</h1>
        <div v-for="record in records">
            <div v-for=" in record"></div>
            <p style="font-size: small;">{{ record.history }}</p>
        </div>


    </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/accountStore';
import { useUserStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted, ref } from 'vue';
const userstore = useUserStore()
const accountstore = useAccountStore()

const records = ref()

onMounted(() => {
    axios({
        method: 'get',
        url: ' http://127.0.0.1:8000/gameApp/test/',
        headers: {
            Authorization: `Token ${accountstore.token}`
        },
    }).then(res => {
        console.log(res)
        records.value = res.data
    })

        .catch(err => console.log(err))
})

</script>

<style scoped></style>