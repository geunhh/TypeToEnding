import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'


export const useAccountStore = defineStore('account', () => {
  const token = ref(null)
  const userInfo = ref(null)
  const userId = ref(null)
  const router = useRouter()
  const BASE_URL = 'http://127.0.0.1:8000'

  // 회원 가입
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
        // console.log('회원가입 성공..')
        // console.log(res.data)
        window.alert("가입되었습니다")
        const password = password1
        logIn({ email, password }) // 가입 완료 되면 바로 로그인 된 채로 메인페이지로 이동
      })
      .catch(err => window.alert("회원 가입에 실패하였습니다"))
  }

  // 로그인
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
        // console.log('로그인 성공..')
        // console.log(res.data)
        window.alert(`환영합니다 ${email}님`)
        token.value = res.data.key
        getUserInfo()
        router.push({ name: 'main' }) // 로그인 성공시 메인 페이지로 이동
        // 원래는 없어도 되지만 회원 가입후 로그인 + 메인페이지 이동을 위해 필요
      })
      .catch(err => window.alert('이메일 또는 비밀번호가 일치하지 않습니다.'))
  }

  // 유저 정보 가져오기
  const getUserInfo = function () {
    axios({
      method: 'get',
      url: `${BASE_URL}/accounts/user-info/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(res => {
        console.log(token.value)
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
      // console.log('로그아웃 성공')
      window.alert("로그아웃 하였습니다")
      token.value = null
      userId.value = null
    }).catch(err => console.log(err))
  }


  return { token, userInfo, userId, signUp, logIn, getUserInfo, logOut }
}, { persist: true })

const useGameRecordStore = defineStore('gameRecord', () => {
  const accountStore = useAccountStore()
  const user_id = ref(null)
  const token = ref(null)

  // 전적검색
  const getUserGameRecord = () => {
    console.log(accountStore.userId.value)
    console.log(accountStore.token.value)

    //   user_id.value = accountStore.userId.value
    //     axios({
    //       method: 'GET',
    //       url: `${BASE_URL}/user_record/`,
    //       headers: {
    //         Authorization: `Token ${token.value}`
    //       },
    //       params: {
    //         user_id:...
    //     }
    //     }).then().catch(err => window.alert('전적 검색에 실패하였습니다.'))
    // }
  }

  return { user_id, token, getUserGameRecord }

})