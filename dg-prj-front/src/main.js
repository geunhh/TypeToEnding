// main.js
import { createApp } from 'vue';
import { createPinia } from 'pinia';
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate';  // 플러그인 import
import App from './App.vue';
import router from './router';
// 부트스트랩
import BootstrapVue3 from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
import '@/assets/styles/global.css';
import '@/assets/styles/styleguide.css';

const app = createApp(App);

// Pinia 인스턴스 생성
const pinia = createPinia();
pinia.use(piniaPluginPersistedstate); // 플러그인 적용

// Vue 애플리케이션에 Pinia와 Router, bootstrap 사용
app.use(pinia);
app.use(router);
app.use(BootstrapVue3)

// npm install bootstrap-vue-3

app.mount('#app');
