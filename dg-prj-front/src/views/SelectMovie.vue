<template>
  <div class="bigbig-container">
    
    <div style="text-align: center;">
      <h1 class="title">Type to Ending</h1>

    </div>
    <div class="big-contianer" >
        <!--  -->
        <div id="carouselExampleControlsNoTouching" class="carousel slide" data-bs-touch="false" 
            style="width: 70rem; text-align: center; margin: 0 auto; " >
          <div class="carousel-inner" >
            <div class="carousel-item" 
                v-for="(movie,index) in moviestore.movies" 
                :key="movie.id" 
                :class="{active: index===0}">
                <img class="poster" :src="`http://127.0.0.1:8000${moviestore.movies[index].poster_path}`" 
                  style="height:60rem ;" v-if="movie.poster_path">
            </div>
          </div>
          <!-- 캐러셀 좌우 버튼 -->
           
          <button class="carousel-control-prev" type="button" 
                  data-bs-target="#carouselExampleControlsNoTouching" data-bs-slide="prev">
            <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" fill="currentColor" class="bi bi-caret-left-fill" viewBox="0 0 16 16">
            <path d="m3.86 8.753 5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z"/>
          </svg>
            
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControlsNoTouching" data-bs-slide="next">
            <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" fill="currentColor" class="bi bi-caret-right-fill" viewBox="0 0 16 16" >
              <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>
            </svg>
            <span class="visually-hidden">Next</span>
          </button> 
        </div> 
        <div style="text-align: center; margin-top: 30px;">
        <button type="button" class="btn btn-danger"  @click="submitMovie"><h2>영화선택</h2></button>

      </div>

        
    </div>
    
  
  
       
  </div>


</template>

<script setup>
import { useMovieStore } from '@/stores/counter';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()
const moviestore = useMovieStore()

// 선택된 영화
const selectedMovieIndex = ref(0)
const totalMovies = ref(null)


onMounted(async() => {
    await moviestore.getMovies()

    // 캐러셀 이벤트 리스너 추가
    const myCarousel = document.getElementById('carouselExampleControlsNoTouching')
    selectedMovieIndex.value = 0

    myCarousel.addEventListener('slide.bs.carousel', (event) => {
      console.log(event)
      updateSelectedMovie(event)
    })
})

// 캐러셀 버튼 누르면 이벤트 발생하면서 함수 실행
const updateSelectedMovie = function (event) {
  totalMovies.value = moviestore.movies.length
  if (event.direction === "left") {
    // 오른쪽 버튼 클릭 시 다음 슬라이드로 이동
    console.log('우')
    selectedMovieIndex.value = (selectedMovieIndex.value + 1) % totalMovies.value;
  } else if (event.direction === "right") {
    // 왼쪽 버튼 클릭 시 이전 슬라이드로 이동
    console.log('좌')
    selectedMovieIndex.value =
      (selectedMovieIndex.value - 1 + totalMovies.value) % totalMovies.value;
  }  


  console.log('ggg', selectedMovieIndex.value)

};

const submitMovie = () => {
  if (moviestore.movies.length > 0) {
    const selected = moviestore.movies[selectedMovieIndex.value];
    moviestore.movieId = selected.id;
    moviestore.movie_name = selected.title;
    moviestore.description = selected.description;
    moviestore.context = selected.context;
    moviestore.poster_path = selected.poster_path;

    // 라운지로 다시 이동. roomID와 함께.
    router.push({name:'LoungeView', params: { roomId : moviestore.roomId}})

  } else {
    alert("영화를 선택해주세요."); // 영화 선택이 안 되었을 경우 경고
  }
}




</script>

<style scoped>
.movie_description_box{
  margin-top: 40px;
  border-radius: 10px; background-color: rgb(56, 48, 48);
  padding: 10px;

}
.description{
    font-size: small
}
.big-contianer{
    padding-inline: 10%;
}
.bigbig-container{
  padding : 5rem ;
}
.title {
    align-self: center;
    color: var(--absolutewhite);
    font-family: var(--font-family-inknut_antiqua);
    font-size: var(--font-size-xxl);
    font-weight: 400;
    letter-spacing: 0;
    line-height: normal;
    min-height: 248px;
    min-width: 816px;
    text-shadow: 0px 4px 4px #00000040;
}
</style>