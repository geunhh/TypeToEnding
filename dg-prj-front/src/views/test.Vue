<template>
    <div class="carousel-item" 
     v-for="(movie, index) in moviestore.movies" 
     :key="movie.id" 
     :class="{active: index === 0}">
    <!-- 현재 영화 -->
        <img class="poster" 
            :src="`http://127.0.0.1:8000${moviestore.movies[index].poster_path}`" 
            style="width:20rem;" 
            v-if="moviestore.movies[index].poster_path">
        
        <!-- 다음 영화 (배열 끝에서는 처음으로 순환) -->
        <img class="poster" 
            :src="`http://127.0.0.1:8000${moviestore.movies[(index + 1) % moviestore.movies.length].poster_path}`" 
            style="width:20rem;" 
            v-if="moviestore.movies[(index + 1) % moviestore.movies.length].poster_path">
        
        <!-- 다다음 영화 -->
        <img class="poster" 
            :src="`http://127.0.0.1:8000${moviestore.movies[(index + 2) % moviestore.movies.length].poster_path}`" 
            style="width:20rem;" 
            v-if="moviestore.movies[(index + 2) % moviestore.movies.length].poster_path">
    </div>
</template>

<script setup>

</script>

<style lang="scss" scoped>

</style>