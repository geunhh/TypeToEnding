<template>
    <div>

        <!-- 비밀번호 변경 모달 -->
        <div class="black-bg" v-if="isUpdatePasswordModalOpen">
            <div class="white-bg">
                <h2>대충 비밀번호 변경 폼</h2>
                <input type="password" v-model="currentPassword" placeholder="현재 비밀번호" />
                <input type="password" v-model="newPassword1" placeholder="새 비밀번호" />
                <input type="password" v-model="newPassword2" placeholder="비밀번호 확인" />
                <button @click.prevent="updatePassword">Update</button>
                <button @click.prevent="closePasswordUpdateModal">Cancel</button>
            </div>
        </div>

        <!-- 유저 정보 업데이트 모달 -->
        <div class="black-bg" v-if="isUpdateUserInfoModalOpen">
            <div class="white-bg">
                <h2>대충 유저정보 변경 폼</h2>
                <form>
                    <p>NickName</p>
                    <input type="text" v-model="newNickname" :placeholder="store.userInfo.name">
                    <p>Age</p>
                    <input type="number" v-model="newAge" min="1" :placeholder="store.userInfo.age" />
                    <p>Sex</p>
                    <select v-model="newSex">
                        <option value="" disabled selected>성별 선택</option>
                        <option value="M">남자</option>
                        <option value="F">여자</option>
                    </select>
                    <br>
                    <input type="submit" @click.prevent="updateUserInfo" value="Update"></input>
                </form>
                <button @click.prevent="closeUpdateUserInfoModal">Cancel</button>
            </div>
        </div>

        <!-- 전적 검색 모달 -->
        <div class="black-bg" v-if="isGameInfoSearchModalOpen">
            <div class="white-bg">
                <h2>대충 전적 검색</h2>
                <button>Update</button><button @click.prevent="isGameInfoSearchModalOpen = false">Cancel</button>
            </div>
        </div>

        <button @click.prevent="backToMain"> |< </button>
                {{ name }}님의 페이지
                <p>NickName : {{ name }}</p>
                <p>Age : {{ age }}</p>
                <p>Sex : {{ sex }}</p>
                <p>Email : {{ email }}</p>
                <p>WinRate : {{ avg_win_point }}</p>

                <button @click="gameInfoSearch"> 전적 보기 </button>
                <br>
                <button @click="isUpdatePasswordModalOpen = true"> Change Password </button>
                <br>
                <button @click.prevent="isUpdateUserInfoModalOpen = true"> Update Profile </button>

    </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/accountStore';
import { useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import axios from 'axios';

const store = useAccountStore()
const router = useRouter()
const isUpdatePasswordModalOpen = ref(false)
const isUpdateUserInfoModalOpen = ref(false)
const isGameInfoSearchModalOpen = ref(false)
const currentPassword = ref(null)
const newPassword1 = ref(null)
const newPassword2 = ref(null)
const BASE_URL = 'http://127.0.0.1:8000'
const newNickname = ref(null)
const newAge = ref(null)
const newSex = ref(null)
const name = ref(null)
const age = ref(null)
const sex = ref(null)
const email = store.userInfo.email
const avg_win_point = store.userInfo.avg_win_point


onMounted(() => {
    store.getUserInfo()
    name.value = store.userInfo.name
    sex.value = store.userInfo.sex
    age.value = store.userInfo.age
})

// token 정보 => userid
const backToMain = () => {
    router.push({
        name: 'main'
    })
}

const gameInfoSearch = () => {
    isGameInfoSearchModalOpen.value = true
}

const updatePassword = () => {
    // 대충 입력받은 비밀번호를 axios 정의하고 던져주기
    if (newPassword1.value != newPassword2.value) {
        window.alert("새로 입력한 두 비밀번호가 서로 일치하지 않습니다")
    }
    else {
        axios({
            method: 'POST',
            url: `${BASE_URL}/api/auth/password/change/`, // 얘는 나중에 장고에서 url 설정하고 다시 돌아오자
            data: {
                old_passowrd: currentPassword.value, // 키가 맞는지도 한번 더 확인하자
                new_password1: newPassword1.value,
                new_password2: newPassword1.value
            },
            headers: {
                "Authorization": `Token ${store.token}`
            }
        }).then(res => {
            window.alert("비밀번호가 성공적으로 변경되었습니다.")
        }).then(() => {
            closePasswordUpdateModal()
        }).catch(err => {
            window.alert("비밀번호변경에 문제가 생겼습니다")
            console.error(err)
        })
    }
}


const updateUserInfo = () => {
    axios({
        method: 'PUT',
        url: `${BASE_URL}/accounts/update-info/`,
        data: {
            name: newNickname.value,
            age: newAge.value,
            sex: newSex.value
        },
        headers: {
            "Authorization": `Token ${store.token}`
        }
    }).then(res => {
        console.log(res.data.user)
        store.userInfo.name = res.data.user.name
        store.userInfo.age = res.data.user.age
        store.userInfo.sex = res.data.user.sex
        window.alert('성공적으로 유저 정보가 업데이트 되었습니다')
        return store.userInfo

    }).then((userInfo) => {
        name.value = userInfo.name
        age.value = userInfo.age
        sex.value = userInfo.sex

    }).then(() => {
        closeUpdateUserInfoModal()
    }).catch(err => window.alert('유저 정보 변경에 문제가 생겼습니다'))
}

const closePasswordUpdateModal = () => {
    isUpdatePasswordModalOpen.value = false
    currentPassword.value = ""
    newPassword1.value = ""
    newPassword2.value = ""
}
const closeUpdateUserInfoModal = () => {
    isUpdateUserInfoModalOpen.value = false
    newNickname.value = null
    newAge.value = null
    newSex.value = null
}

</script>

<style scoped>
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