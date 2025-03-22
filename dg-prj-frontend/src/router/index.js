import ComeScenario from '@/components/ComeScenario.vue'
import CreateMovie from '@/components/CreateMovie.vue'
import EvaluationView from '@/components/EvaluationView.vue'
import Recordtest from '@/components/recordtest.vue'
import GamePlayView from '@/views/GamePlayView.vue'
import LoungeView from '@/views/LoungeView.vue'
import MainPage from '@/views/MainPage.vue'
import ProfilePageView from '@/views/ProfilePageView.vue'
import ResultView from '@/views/ResultView.vue'
import RoundResult from '@/views/RoundResult.vue'
import SelectMovie from '@/views/SelectMovie.vue'
import SignUpView from '@/views/SignUpView.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/test',
      name: 'test',
      component: Recordtest
    },
    {
      path: '/',
      name: 'main',
      component: MainPage
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/profile=:userId',
      name: 'ProfilePageView',
      component: ProfilePageView
    },
    {
      path: '/lounge/:roomId',
      name: 'LoungeView',
      component: LoungeView,
      props: true,
    },
    {
      path: '/movieselect',
      name: 'SelectMovie',
      component: SelectMovie
    },
    {
      path: '/loading',
      name: 'loading',
      component: ComeScenario
    },
    {
      path: '/typetoend/:roomId',
      name: 'GamePlayView',
      component: GamePlayView,
    },
    {
      path: '/evaluation',
      name: 'evaluation',
      component: EvaluationView,
    },
    {
      path: '/roundresult',
      name: 'roundresult',
      component: RoundResult,
    },
    {
      path: '/ResultPage',
      name: 'ResultPage',
      component: ResultView,
    },
    {
      path: '/CreateMovie',
      name: 'CreateMovie',
      component: CreateMovie
    }
  ],

})



export default router
