<template>
    <div>
        <h2 style="margin-top: -10px;">Type to Ending</h2>
    </div>
    <div class="big-contianer">
        {{ moviestore.roomId }}
    <form @submit.prevent="submitMovie">
    <div v-for="movie in moviestore.movies" :key="movie.id">
        <!-- 영화 정보 렌더링 -->
        <p style="text-align: left;">{{movie.title}} <input
          type="radio"
          :value="movie"
          v-model="selectedMovie"
          name="selectedMovie"
        /></p>
        <p class="description">{{movie.description}}</p>
        <hr>
    </div>
    <button type="submit">영화 선택</button>

    </form>
    </div>


</template>

<script setup>
import { useMovieStore, useUserStore } from '@/stores/counter';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()
const store = useUserStore()
const moviestore = useMovieStore()

const selectedMovie = ref(null)

onMounted(() => {
    moviestore.getMovies()
})

const submitMovie = () => {
  if (selectedMovie.value) {
    // 선택한 영화 정보 저장
    moviestore.movieId = selectedMovie.value.id; 
    moviestore.movie_name = selectedMovie.value.title
    moviestore.description = selectedMovie.value.description
    moviestore.context = selectedMovie.value.context
    moviestore.poster_path = selectedMovie.value.poster_path

    // 라운지로 다시 이동. roomID와 함께.
    router.push({name:'LoungeView', params: { roomId : moviestore.roomId}})

  } else {
    alert("영화를 선택해주세요."); // 영화 선택이 안 되었을 경우 경고
  }
}




</script>

<style scoped>
.description{
    font-size: small
}
.big-contianer{
    padding-inline: 10%;
}
</style>