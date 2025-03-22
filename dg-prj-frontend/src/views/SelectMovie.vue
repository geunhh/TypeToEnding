<template>
  <video autoplay loop muted class="background-video" ref="backgroundVideo">
    <source src="@/assets/movies/background.mp4" type="video/mp4">
  </video>
  <div class="bigbig-container" v-if="moviestore.movies != null">


    <div style="text-align: center;">
      <h1 class="title">Type to Ending</h1>
      <!-- {{ originalMovielist }} -->
    </div>
    <div class="big-contianer">
      <!--  -->
      <div id="carouselExampleControlsNoTouching" class="carousel slide" data-bs-touch="false"
        style="width: 40rem; text-align: center; margin: 0 auto; ">
        <div class="carousel-inner">

          <div class="carousel-item" v-for="(movie, index) in originalMovielist" :key="movie.id"
            :class="{ active: index === 0 }" v-if="!isCustom">
            <img class="poster" :src="`http://127.0.0.1:8000${originalMovielist[index].poster_path}`"
              style="height:35rem ;" v-if="movie.poster_path">
            <img class="poster" src='@/assets/selectimg.jpeg' v-else style="height: 35rem;">

          </div>

          <div class="carousel-item" v-for="(movie, index) in customMovielist" :class="{ active: index === 0 }" v-else>
            <!-- <img class="poster" :src="`http://127.0.0.1:8000${customMovielist[index].poster_path}`"
              style="height:35rem ;" v-if="movie.poster_path"> -->
            <!-- <img class="poster" src='@/assets/selectimg.jpeg' v-else style="height: 60rem;"> -->
            <div style="height: 35rem;" >
              <h1 style="color: white;">{{ movie.title }}</h1>
            </div>
            <!-- 이건 포스터 만약 있으면, 포스터 보여주고 없으면 이름만 보여주면 될듯. -->
          </div>


        </div>
        <!-- 캐러셀 좌우 버튼 -->
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControlsNoTouching"
          data-bs-slide="prev">
          <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor"
            class="bi bi-caret-left-fill" viewBox="0 0 16 16">
            <path
              d="m3.86 8.753 5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z" />
          </svg>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControlsNoTouching"
          data-bs-slide="next">
          <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor"
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

  <!-- 댓글 창  -->
  <div class="comment-container">
    <p class="d-inline-flex gap-1">
      <button class="btn btn-primary " type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample"
        aria-expanded="false" aria-controls="collapseExample">
        Comment list
      </button>
    </p>
    <div class="collapse collapse-panel" id="collapseExample">
      <div class="card card-body" style="color: black;">
        <h5>Comments</h5>
        <ul>
          <li v-for="comment in comments" :key="comment.id">
            <strong style="background-color: rgba(50, 0, 0, 0.5); border-radius: 50%;">{{ comment.user.name }}</strong> <br> - {{ comment.content }}
          </li>
        </ul>
        <p v-if="comments.length === 0">No comments available for this movie.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/accountStore';
import { useMovieStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted, ref, watch } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()
const moviestore = useMovieStore()
const accountstore = useAccountStore()
// 선택된 영화
const selectedMovieIndex = ref(0)
const totalMovies = ref(null)

const isCustom = ref(false)

const customMovielist = ref([])
const originalMovielist = ref([])

// 댓글 목록
const comments = ref([])


onMounted(async () => {
  await moviestore.getMovies()
  customMovielist.value = moviestore.movies.filter((movie) => movie.creator !== 1)
  originalMovielist.value = moviestore.movies.filter((movie) => movie.creator === 1)
  // console.log('커스텀', customMovielist)
  // console.log(originalMovielist)

  // 첫 번째 영화 댓글 가져오기
  if (originalMovielist.value.length > 0) {
    getComments(originalMovielist.value[0].id)
  }

  // 초기 총 영화 수 설정
  totalMovies.value = originalMovielist.value.length

  const myCarousel = document.getElementById('carouselExampleControlsNoTouching')
  selectedMovieIndex.value = 0

  myCarousel.addEventListener('slide.bs.carousel', (event) => {
    updateSelectedMovie(event)
  })
})

// 감시
watch(
  () => moviestore.movies,
  (newMovies) => {
    customMovielist.value = newMovies.filter((movie) => movie.creator !== 1)
    originalMovielist.value = newMovies.filter((movie) => movie.creator === 1);
  }
)


// 댓글 가져오는 함수
const getComments = function (movieId) {
  return axios({
    method: 'get',
    url: `http://127.0.0.1:8000/gameApp/comment/${movieId}/`,
    headers: {
      Authorization: `Token ${accountstore.token}`
    }
  })
    .then(res => {
      console.log(res)
      comments.value = res.data
      return res.data
    })
    .catch(err => {
      console.log(err)
      comments.value = []
    })


}

// 캐러셀 버튼 누르면 이벤트 발생하면서 함수 실행
const updateSelectedMovie = function (event) {
  const currentList = isCustom.value ? customMovielist.value : originalMovielist.value;
  // console.log('먀먀먀')
  // 현재 보고 있는 리스트에 따라 총 영화 수 설정
  totalMovies.value = isCustom.value ? customMovielist.value.length : originalMovielist.value.length

  // 방향에 따라 선택된 영화 인덱스 업데이트
  if (event.direction === "left") {
    selectedMovieIndex.value = (selectedMovieIndex.value + 1) % totalMovies.value;
  } else if (event.direction === "right") {
    selectedMovieIndex.value = (selectedMovieIndex.value - 1 + totalMovies.value) % totalMovies.value;
  }

  const selectedmovie = currentList[selectedMovieIndex.value]
  // console.log(selectedmovie)
  if (selectedmovie) {
    getComments(selectedmovie.id)
      .then(data => {
        // console.log('댓글 업데이트',data)
        comments.value = data
      })
      .catch(err => console.log('댓글 업데이트 실패', err))

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
.comment-container {
  position: fixed;
  top: 11rem;
  right: 4rem; /* "Comment list" 버튼의 위치를 유지 */
  z-index: 9999;
}

.btn-primary {
  background: #1A1A1A;
  border: 1px solid #500010;
  padding: 0.8rem 1.5rem;
  border-radius: 8px;
  color: #fff;
  font-weight: 500;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  background: #500010;
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(80, 0, 10, 0.4);
}

.collapse-panel {
  position: absolute;
  top: 3rem;
  right: 0;
  width: 400px; /* 댓글 창의 너비를 조정 (예: 400px로 확장) */
}

.card {
  background: #1A1A1A;
  border: 1px solid rgba(173, 154, 157, 0.3);
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  width: 100%; /* 카드가 댓글 창 전체 너비를 사용하도록 설정 */
}

.card-body {
  padding: 1.5rem;
  color: #fff !important;
}

.card-body ul {
  list-style: none;
  padding: 0;
  margin: 0;
  overflow-y: auto; /* 댓글이 많을 경우 스크롤을 추가 */
  max-height: 300px; /* 댓글 목록의 최대 높이를 제한 (선택 사항) */
}

.card-body li {
  padding: 0.8rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  transition: all 0.3s ease;
}

.card-body li:hover {
  background: rgba(131, 2, 19, 0.1);
}

.card-body p {
  color: #8B8680;
  text-align: center;
  margin: 1rem 0 0;
}

/* "Comment list" 버튼 위치 고정 */
.comment-container > p {
  margin: 0;
}

.bigbig-container {
  padding: 3rem;
  background: rgba(0, 0, 0, 0.2);
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
  width: 70px;
  height: 70px;
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
  border: 2px solid rgba(173, 154, 157, 0.3);
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
  background: linear-gradient(to right, var(--black10), var(--black06));
  padding: 2rem;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}
.collapse-panel ul::-webkit-scrollbar {
  width: 10px; /* 스크롤바 너비 */
}
.collapse-panel ul::-webkit-scrollbar-track {
  background: #1A1A1A; /* 스크롤바 트랙 (배경) 색상 */
}

.collapse-panel ul::-webkit-scrollbar-thumb {
  background: #830213; /* 스크롤바 색상 */
  border-radius: 5px; /* 스크롤바 둥글기 */
}
.collapse-panel ul::-webkit-scrollbar-thumb:hover {
  background: #5f0612; /* 스크롤바 위에 마우스를 올렸을 때 색상 */
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