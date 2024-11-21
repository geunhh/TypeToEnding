// main.js
import { createApp } from 'vue';
import { createPinia } from 'pinia';
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate';  // 플러그인 import
import App from './App.vue';
import router from './router';

const app = createApp(App);

// Pinia 인스턴스 생성
const pinia = createPinia();
pinia.use(piniaPluginPersistedstate); // 플러그인 적용

// Vue 애플리케이션에 Pinia와 Router 사용
app.use(pinia);
app.use(router);

app.mount('#app');
