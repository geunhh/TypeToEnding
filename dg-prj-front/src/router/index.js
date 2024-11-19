import LoungeView from '@/views/LoungeView.vue'
import MainPage from '@/views/MainPage.vue'
import SignUpView from '@/views/SignUpView.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path : '/',
      name : 'main',
      component : MainPage
    },
    {
      path : '/signup',
      name : 'SignUpView',
      component : SignUpView
    },
    {
      path : '/lounge/:roomId',
      name : 'LoungeView',
      component :LoungeView
    }


  ],
})

export default router
