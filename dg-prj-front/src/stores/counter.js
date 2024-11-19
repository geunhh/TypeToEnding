import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'


export const useUserStore = defineStore('user', () => {
  const token = ref(null)
  const userId = ref(null)
  const router = useRouter()
  const movieId = ref()

  const signUp = function (payload) {    
    const email = payload.email
    const password1 = payload.password1
    const password2 = payload.password2
    

    axios({
      method : 'post',
      url: `http://127.0.0.1:8000/accounts/signup/`,
      data : {
         email, password1,password2
      }
    })
    .then (res=>{ 
      console.log('회원가입 성공..')
      console.log(res.data)
      router.push({ name:'main' })
      
    })
    .catch(err => console.log(err.response))
  }

  const logIn = function (payload) {
    const email = payload.email
    const password = payload.password

    axios({
      method:'post',
      url: `http://127.0.0.1:8000/accounts/login/`,
      data : {
         email, password
      }
    })
    .then (res=>{ 
      console.log('로그인 성공..')
      console.log(res.data)  
      token.value=res.data.key
      getUserInfo()
    })
    .catch(err => console.log(err))
  }

  const getUserInfo = function () {
    axios({
      method : 'get',
      url: `http://127.0.0.1:8000/accounts/user-info/`,
      headers : {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => {
      console.log('사용자 정보 가져오기 성공')
      console.log(res.data)
      userId.value = res.data.user_id
    })
    
  }

  return {  signUp , logIn, token, getUserInfo, userId, movieId}
},{persist:true})
