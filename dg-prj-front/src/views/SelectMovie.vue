<template>
  <div class="bigbig-container">
    <div style="text-align: center;">
      <h1 class="title">Type to Ending</h1>
      <!-- {{ originalMovielist }} -->
    </div>
    <div class="big-contianer">
      <!--  -->
      <div id="carouselExampleControlsNoTouching" class="carousel slide" data-bs-touch="false"
        style="width: 70rem; text-align: center; margin: 0 auto; ">
        <div class="carousel-inner">

          <div class="carousel-item" v-for="(movie, index) in originalMovielist" :key="movie.id"
            :class="{ active: index === 0 }" v-if="!isCustom">
            <img class="poster" :src="`http://127.0.0.1:8000${originalMovielist[index].poster_path}`"
              style="height:60rem ;" v-if="movie.poster_path">
            <img class="poster" src='@/assets/selectimg.jpeg' v-else style="height: 60rem;">

          </div>

          <div class="carousel-item" v-for="(movie, index) in customMovielist" :key="movie.id"
            :class="{ active: index === 0 }" v-else>
            <img class="poster" :src="`http://127.0.0.1:8000${customMovielist[index].poster_path}`"
              style="height:60rem ;" v-if="movie.poster_path">
            <!-- <img class="poster" src='@/assets/selectimg.jpeg' v-else style="height: 60rem;"> -->
            <div style="height: 60rem;" v-else>
              <h1 style="color: white;">{{ movie.title }}</h1>
            </div>
            <!-- 이건 포스터 만약 있으면, 포스터 보여주고 없으면 이름만 보여주면 될듯. -->
          </div>


        </div>
        <!-- 캐러셀 좌우 버튼 -->
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControlsNoTouching"
          data-bs-slide="prev">
          <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" fill="currentColor"
            class="bi bi-caret-left-fill" viewBox="0 0 16 16">
            <path
              d="m3.86 8.753 5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z" />
          </svg>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControlsNoTouching"
          data-bs-slide="next">
          <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" fill="currentColor"
            class="bi bi-caret-right-fill" viewBox="0 0 16 16">
            <path
              d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z" />
          </svg>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
      <!-- 버튼 목록 -->
      <div style="text-align: center; margin-top: 30px;">
        <button type="button" class="btn btn-danger" @click="submitMovie">
          <h2>영화선택</h2>
        </button>
        <button type="button" class="btn btn-primary" @click="isCustom = !isCustom">
          <h3>{{ isCustom ? 'Origin' : 'Custom' }}</h3>
        </button>
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

const isCustom = ref(false)

const customMovielist = ref()
const originalMovielist = ref()


onMounted(async () => {
  await moviestore.getMovies()

  // 영화 리스트 구분. 일단 14번이 admin이라 이렇게 적어둠. 나중에 db갈거나 하면 1로 바꾸면 될듯.
  customMovielist.value = moviestore.movies.filter((movie) => movie.creator !== null)
  originalMovielist.value = moviestore.movies.filter((movie) => movie.creator === null)
  console.log('커스텀', customMovielist)
  console.log(originalMovielist)

  // 초기 총 영화 수 설정
  totalMovies.value = originalMovielist.value.length

  const myCarousel = document.getElementById('carouselExampleControlsNoTouching')
  selectedMovieIndex.value = 0

  myCarousel.addEventListener('slide.bs.carousel', (event) => {
    updateSelectedMovie(event)
  })
})

// 캐러셀 버튼 누르면 이벤트 발생하면서 함수 실행
const updateSelectedMovie = function (event) {
  // 현재 보고 있는 리스트에 따라 총 영화 수 설정
  totalMovies.value = isCustom.value ? customMovielist.value.length : originalMovielist.value.length

  if (event.direction === "left") {
    selectedMovieIndex.value = (selectedMovieIndex.value + 1) % totalMovies.value;
  } else if (event.direction === "right") {
    selectedMovieIndex.value = (selectedMovieIndex.value - 1 + totalMovies.value) % totalMovies.value;
  }
}

const submitMovie = () => {
  // 현재 보고 있는 리스트에서 선택된 영화 가져오기 
  // isCustom에 따라서 가져옴.
  const currentList = isCustom.value ? customMovielist.value : originalMovielist.value;

  // currentList 없거나 하면 에러 뜰 거 같아서 넣어둠.
  if (currentList && currentList.length > 0) {
    const selected = currentList[selectedMovieIndex.value];

    moviestore.movieId = selected.id;
    moviestore.movie_name = selected.title;
    moviestore.description = selected.description;
    moviestore.context = selected.context;
    moviestore.poster_path = selected.poster_path;

    router.push({ name: 'LoungeView', params: { roomId: moviestore.roomId } })
  }
  else {
    alert("영화를 선택해주세요.");
  }
}




</script>

<style scoped>
.bigbig-container {
  padding: 3rem;
  background: var(--black10);
  min-height: 100vh;
}

.title {
  color: #ffffff;
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 3rem;
  text-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
  position: relative;
}

.title::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 100px;
  height: 4px;
  background: var(--red45);
}

/* 캐러셀 스타일링 */
.carousel {
  background: var(--black06);
  border: 1px solid var(--abbey);
  border-radius: 15px;
  padding: 1.5rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.carousel-item {
  border-radius: 12px;
  overflow: hidden;
}

.poster {
  border: 1px solid var(--abbey);
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s ease;
}

.poster:hover {
  transform: scale(1.02);
}

/* 캐러셀 버튼 */
.carousel-control-prev,
.carousel-control-next {
  width: 80px;
  height: 80px;
  background: rgba(131, 2, 19, 0.2);
  border-radius: 50%;
  opacity: 0.8;
  transition: all 0.3s ease;
}

.carousel-control-prev:hover,
.carousel-control-next:hover {
  background: rgba(131, 2, 19, 0.4);
  opacity: 1;
}

.bi-caret-left-fill,
.bi-caret-right-fill {
  color: #ffffff;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.3));
}

/* 버튼 스타일링 */
.btn-danger {
  background: transparent;
  border: 2px solid var(--red45);
  padding: 1rem 2rem;
  border-radius: 8px;
  margin: 0 1rem;
  transition: all 0.3s ease;
}

.btn-danger:hover {
  background: var(--red45);
  border: 2px solid var(--red45);
  transform: translateY(-2px);
  box-shadow: 0 4px 15px var(--red45);
}

.btn-primary {
  background: var(--black10);
  border: 2px solid var(--red45);
  padding: 1rem 2rem;
  border-radius: 8px;
  margin: 0 1rem;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  border: 2px solid var(--red45);
  background: var(--red45);
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(131, 2, 19, 0.4);
}

.btn h2,
.btn h3 {
  margin: 0;
  color: #ffffff;
  font-weight: 500;
}

/* 영화 제목 스타일링 (포스터 없을 때) */
.carousel-item h1 {
  background: linear-gradient(to right, var(--black10), #2d2d2d);
  padding: 2rem;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

@media (max-width: 768px) {
  .bigbig-container {
    padding: 1rem;
  }

  .title {
    font-size: 2rem;
    min-width: auto;
  }
}
</style>