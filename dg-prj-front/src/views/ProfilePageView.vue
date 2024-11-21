<template>
    <div>
        <button @click.prevent="backToMain">
            |< </button>
                <!-- 가만... 가입할때 닉네임도 받아야할듯? -->
                <!-- 안그러면 프로필 페이지에 들어갔을 때 미리 설정되어있을 이름이 없다... -->
                {{ store.userId }}님의 페이지
                <!-- <p v-if="...">NickName : {{ }}</p>
                <p v-if="...">Age : {{ }}</p>
                <p v-if="...">Sex : {{ }}</p>
                <p v-if="...">Email : {{ }}</p>
                <p v-if="...">WinRate : {{ }}</p> -->

                <button>
                    전적 보기
                </button>
                <button>
                    Change Password
                </button>
                <button>
                    Update Profile
                </button>

    </div>
</template>

<script setup>
import { useUserStore } from '@/stores/counter';
import { useRoute, useRouter, RouterLink } from 'vue-router'
import { ref } from 'vue'

const store = useUserStore()
const route = useRoute()
const router = useRouter()
// token 정보 => userid
const backToMain = () => {
    router.push({
        name: 'main'
    })
}

</script>

<style lang="scss" scoped></style>