import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'


export const useAccountStore = defineStore('user', () => {
  const token = ref(null)
  const userInfo = ref(null)
  const userId = ref(null)
  const router = useRouter()
  const BASE_URL = 'http://127.0.0.1:8000'

  const signUp = function (payload) {
    const email = payload.email
    const password1 = payload.password1
    const password2 = payload.password2
    const name = payload.name


    axios({
      method: 'post',
      url: `${BASE_URL}/accounts/signup/`,
      data: {
        email, password1, password2, name
      }
    })
      .then(res => {
        console.log('회원가입 성공..')
        console.log(res.data)
        const password = password1
        logIn({ email, password }) // 가입 완료 되면 바로 로그인 된 채로 메인페이지로 이동
      })
      .catch(err => console.log(err.response))
  }

  const logIn = function (payload) {
    const email = payload.email
    const password = payload.password

    axios({
      method: 'post',
      url: `${BASE_URL}/accounts/login/`,
      data: {
        email, password
      }
    })
      .then(res => {
        console.log('로그인 성공..')
        console.log(res.data)
        token.value = res.data.key
        getUserInfo()
        router.push({ name: 'main' }) // 로그인 성공시 메인 페이지로 이동
        // 원래는 없어도 되지만 회원 가입후 로그인 + 메인페이지 이동을 위해 필요
      })
      .catch(err => console.log(err))
  }

  const getUserInfo = function () {
    axios({
      method: 'get',
      url: `${BASE_URL}/accounts/user-info/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(res => {
        console.log('사용자 정보 가져오기 성공')
        userId.value = res.data.user_id
        userInfo.value = res.data
      })
  }

  // 로그아웃 함수
  const logOut = () => {
    axios({
      method: 'post',
      url: `${BASE_URL}/accounts/logout/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    }).then(() => {
      console.log('로그아웃 성공')
      token.value = null
      userId.value = null
    }).catch(err => console.log(err))
  }

  return { signUp, logIn, token, getUserInfo, userId, logOut, userInfo }
}, { persist: true })
