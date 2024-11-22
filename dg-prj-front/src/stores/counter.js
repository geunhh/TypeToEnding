import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useAccountStore } from './accountStore'

// 유저 정보 및 함수 관리 스토어
export const useUserStore = defineStore('user', () => {
  const token = ref(null)
  const userId = ref(null)
  const router = useRouter()
  const movieId = ref()
  const BASE_URL = 'http://127.0.0.1:8000'


  // 회원가입 함수
  const signUp = function (payload) {
    const email = payload.email
    const password1 = payload.password1
    const password2 = payload.password2

    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/accounts/signup/`,
      data: {
        email, password1, password2
      }
    }).then(res => {
      console.log('회원가입 성공..')
      console.log(res.data)

    }).catch(err => console.log(err.response))
  }
  // 로그인 함수
  const logIn = function (payload) {
    const email = payload.email
    const password = payload.password

    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/accounts/login/`,
      data: {
        email, password
      }
    }).then(res => {
      console.log('로그인 성공..')
      console.log(res.data)
      token.value = res.data.key
      getUserInfo()

    }).catch(err => console.log(err))
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

  // 유저 정보 가져오기 
  // 로그인했을 때는 회원에게 부여된 토큰 정보만 가져오기 때문에 토큰을 다시 axios 보내 회원정보를 역참조.
  const getUserInfo = function () {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/user-info/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(res => {
        console.log('사용자 정보 가져오기 성공')
        console.log(res.data)
        userId.value = res.data.user_id
      })

  }

  return { signUp, logIn, token, getUserInfo, userId, movieId, logOut }
}, { persist: true })

// 영화 정보 및 함수 관리 스토어
export const useMovieStore = defineStore('movie', () => {

  const movies = ref(null) // 영화 전체 목록 -> 영화 선택에서 사용.
  const userstore = useUserStore()
  const accountstore = useAccountStore()
  // 선택한 영화 정보
  const movieId = ref(null)
  const movie_name = ref(null)
  const roomId = ref(null)
  const description = ref(null)
  const context = ref(null)
  const poster_path = ref(null)

  // 영화 전체 정보 가져오기.
  const getMovies = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/gameApp/movielist/',
      headers: {
        Authorization: `Token ${accountstore.token}`
      },
    }).then(res => {
      console.log('영화 정보 가져오기 성공')
      console.log(res.data)
      movies.value = res.data
    }).catch(err => console.log(err))
  }
  return { getMovies, movies, movie_name, movieId, description, context, poster_path, roomId }
}, { persist: true })

export const useGameStore = defineStore('game', () => {
  const userstore = useUserStore()
  const moviestore = useMovieStore()
  const accountstore = useAccountStore()
  const game_id = ref(null)
  const game_round = ref(0)
  const initial_question = ref(null)
  const user_action1 = ref(null)
  const next_situation = ref(null)

  const getInitial = function () {
    console.log(moviestore.movieId.value)

    axios({
      method: 'post',
      url: "http://127.0.0.1:8000/gameApp/start_game/",
      headers: {
        Authorization: `Token ${accountstore.token}`
      },
      data: { movie_id: moviestore.movieId, } // 선택된 영화 ID를 이 변수에 담아 전송}
    })
      .then(res => {
        console.log(res)
        initial_question.value = res.data.initial_question
        game_id.value = res.data.game_id
      })
      .catch(err => {
        console.log(err)
        console.log(moviestore.movieId.value)
        console.log(userstore.token.value)


      })


  }
  return {
    getInitial, initial_question, game_id, game_round,
    user_action1, next_situation
  }

}, { persist: true })