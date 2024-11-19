<template>

  <div style="background-color: #1e1e1e;">
    <RouterLink :to="{name:'main'}">메인</RouterLink>
    <div class="title">
      <RouterView/>   
    </div>  
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';


</script>

<style>
.title {
  text-align: center;
  font-size: xx-large;
}
html {
  color: white;
  background-color: #1e1e1e;
}

</style>