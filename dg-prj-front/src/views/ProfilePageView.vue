<template>
    <div class="">
        <div class="container-center-horizontal--profile">
            <video autoplay loop muted class="background-video">
                <source src="@/assets/movies/background.mp4" type="video/mp4">
            </video>
            <div class="record screen">
                <div class="flex-col">
                    <div class="overlap-group">
                        <div class="sub-container-2">
                            <div class="container">
                                <div class="sub-container-3">
                                    <h1
                                        class="heading-2 valign-text-middle heading-4 manrope-medium-mountain-mist-24px">
                                        {{ name }}님의 프로필 페이지
                                    </h1>
                                </div>
                            </div>
                            <div class="container">
                                <div class="sub-container">
                                    <div class="heading manrope-medium-mountain-mist-16px">닉네임</div>
                                </div>
                                <div class="sub-container-1">
                                    <div class="container-1">
                                        <div class="text manrope-medium-white-14px">{{ name }}</div>
                                    </div>
                                </div>
                            </div>
                            <div class="container">
                                <div class="sub-container">
                                    <div class="heading manrope-medium-mountain-mist-16px">나이</div>
                                </div>
                                <div class="sub-container-1">
                                    <div class="container-1">
                                        <p class="text manrope-medium-white-14px">{{ age !== null ? age : "?" }}</p>
                                    </div>
                                </div>
                            </div>
                            <div class="container">
                                <div class="sub-container">
                                    <div class="heading manrope-medium-mountain-mist-16px">성별</div>
                                </div>
                                <div class="sub-container-1">
                                    <div class="container-1">
                                        <div class="text manrope-medium-white-14px">{{ sex !== null ? sex : "?" }}</div>
                                    </div>
                                </div>
                            </div>
                            <div class="container">
                                <div class="sub-container">
                                    <div class="heading manrope-medium-mountain-mist-16px">이메일</div>
                                </div>
                                <div class="sub-container-1">
                                    <div class="container-4">
                                        <div class="text manrope-medium-white-14px">{{ email }}</div>
                                    </div>
                                </div>
                            </div>
                            <div class="container-5">
                                <div class="sub-container-4">
                                    <div class="heading manrope-medium-mountain-mist-16px">채택률</div>
                                </div>
                                <div class="sub-container-5">
                                    <div class="container-6">
                                        <div class="heading-3 heading-4 manrope-semi-bold-white-16px">
                                            {{ avg_win_point !== null ? avg_win_point : "0 채택 / 0 폐기" }}
                                        </div>
                                        <div class="sub-container-6">
                                            <div class="container-7">
                                                <div v-if="avg_win_rate">
                                                    <img v-for="i in redStars" :key="i" class="star-class"
                                                        src="@/assets/icons/red-star.png" alt="red-star">
                                                    <img v-if="halfStar" class="star-class"
                                                        src="@/assets/icons/half-star.png" alt="half-star">
                                                    <img v-for="i in grayStars" :key="i" class="star-class"
                                                        src="@/assets/icons/gray-star.png" alt="gray-star">
                                                </div>
                                                <div v-else>
                                                    <img v-for="i in 5" :key="i" class="star-class"
                                                        src="@/assets/icons/gray-star.png" alt="gray-star">
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="container-2">
                                <button class="game-record-button" @click.prevent="handleGameInfoSearchModal">
                                    <p class="cancel">{{ !isGameInfoSearchModalOpen ? "전적 보기" : "전적 닫기" }}</p>
                                </button>
                            </div>
                            <div class="container-2">
                                <button class="red-button-common" @click.prevent="handleUpdatePasswordModal">
                                    <p class="option-common">비밀번호 변경</p>
                                </button>
                            </div>
                            <div class="container-2">
                                <button class="red-button-common" @click.prevent="handleUpdateUserInfoModal">
                                    <p class="option-common">프로필 수정</p>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
                <form class="form" v-if="isUpdateUserInfoModalOpen && !isUpdatePasswordModalOpen">
                    <div class="items-container">
                        <div class="container-3">
                            <div class="heading-1 heading-4 manrope-semi-bold-white-18px">닉네임</div>
                            <div class="input-field">
                                <input class="text-2 text-5 input-box manrope-normal-mountain-mist-18px" type="text"
                                    v-model="newNickname" :placeholder="store.userInfo.name">
                            </div>
                        </div>
                    </div>
                    <div class="items-container">
                        <div class="container-3">
                            <div class="heading-1 heading-4 manrope-semi-bold-white-18px">나이</div>
                            <div class="input-field">
                                <input class="text-2 text-5 input-box manrope-medium-mountain-mist-18px"
                                    v-model="newAge" :placeholder="store.userInfo.age || '?'">
                            </div>
                        </div>
                    </div>

                    <div class="items-container">
                        <div class="container-3">
                            <div class="heading-1 heading-4 manrope-semi-bold-white-18px">성별</div>
                            <div class="btn-group">
                                <button class="sex button-sex-select btn btn-secondary btn-lg" type="button">
                                    {{ newSex === 'M' ? '남자' : newSex === 'F' ? '여자' : '?' }}
                                </button>
                                <button type="button"
                                    class="dropdown-sex button-sex-select btn btn-lg btn-secondary dropdown-toggle dropdown-toggle-split"
                                    data-bs-toggle="dropdown" aria-expanded="false">
                                    <span class="visually-hidden">Toggle Dropdown</span>
                                </button>
                                <ul class="dropdown-menu dropdown-menu-end">
                                    <li><button @click="selectSex('M')" class="dropdown-item" type="button">남자</button>
                                    </li>
                                    <li><button @click="selectSex('F')" class="dropdown-item" type="button">여자</button>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <div class="container-2">
                        <button class="red-button-common" @click.prevent="updateUserInfo">
                            <p class="option-common">수정하기</p>
                        </button>
                    </div>
                    <div class="container-2">
                        <button class="cancel-button" @click.prevent="closeUpdateUserInfoModal">
                            <p class="cancel">취소</p>
                        </button>
                    </div>
                </form>
                <!-- 여기까지가 유저정보 모달 -->
                <!-- 아래부터는 비밀번호 모달 -->
                <form class="form" v-if="isUpdatePasswordModalOpen && !isUpdateUserInfoModalOpen">
                    <div class="items-container">
                        <div class="container-3">
                            <div class="heading-1 heading-4 manrope-semi-bold-white-18px">이전 비밀번호</div>
                            <div class="input-field">
                                <input type="password" class="input-box text-2 text-5 manrope-normal-mountain-mist-18px"
                                    placeholder="이전 비밀번호를 입력해주세요" v-model="currentPassword">
                            </div>
                        </div>
                    </div>
                    <div class="items-container">
                        <div class="container-3">
                            <div class="heading-1 heading-4 manrope-semi-bold-white-18px">새 비밀번호</div>
                            <div class="input-field">
                                <input type="password" class="input-box text-2 text-5 manrope-normal-mountain-mist-18px"
                                    placeholder="새 비밀번호를 입력해주세요" v-model="newPassword1">
                            </div>
                        </div>
                    </div>
                    <div class="items-container">
                        <div class="container-3">
                            <div class="heading-1 heading-4 manrope-semi-bold-white-18px">비밀번호 확인</div>
                            <div class="input-field">
                                <input type="password" class="input-box text-2 text-5 manrope-normal-mountain-mist-18px"
                                    placeholder="비밀번호를 확인해주세요" v-model="newPassword2">
                            </div>
                        </div>
                    </div>
                    <div class="container-2">
                        <button class="red-button-common" @click.prevent="updatePassword">
                            <p class="option-common manrope-semi-bold-white-18px">변경</p>
                        </button>
                    </div>
                    <div class="container-2">
                        <button class="cancel-button" @click.prevent="isUpdatePasswordModalOpen = false">
                            <p class="cancel manrope-semi-bold-white-18px">취소</p>
                        </button>
                    </div>
                </form>
                <!-- 여기까지가 비밀번호 모달 -->
                <!-- 아래부터는 전적검색 모달 -->
                <div class="overlap-group-game-info" v-if="isGameInfoSearchModalOpen">
                    <div class="container-7-game-info">

                        <!-- 영화 필터링 기능 -->
                        <div class="sub-container-9-game-info">
                            <div class="text-container">
                                <p class="game-result">{{ name }}님의 전적</p>
                            </div>
                            <div class="dropdown">
                                <button class="btn btn-secondary dropdown-toggle button-4-game-info" type="button"
                                    data-bs-toggle="dropdown" aria-expanded="false">
                                    {{ SelectedMovies || 'All Movies' }}
                                </button>
                                <ul class="dropdown-menu dropdown-menu-end">
                                    <li v-for="(option, index) in playedMovies" :key="index">
                                        <button class="dropdown-item" type="button" @click="selectMovie(option)">{{
                                            option
                                        }}</button>
                                        <div class="dropdown-divider" v-if="index !== playedMovies.length - 1"></div>
                                    </li>
                                </ul>
                            </div>
                        </div>

                        <!-- 전적 띄워주는 기능 -->
                        <div class="sub-container-10">
                            <div class="container-8-game-info" v-if="totalGameRecordsFiltered.length > 0">
                                <div class="number-game-info-summary">요약</div>
                                <div class="sub-container-2-game-info">
                                    <div class="container-9">
                                        <div class="sub-container-3"></div>
                                    </div>
                                    <div class="paragraph manrope-normal-mountain-mist-18px">
                                        <p class="category-heading">플레이한 영화</p>
                                        <p v-if="totalGameRecordsFiltered[currentPage]">{{
                                            totalGameRecordsFiltered[currentPage].movie.title }}</p>
                                        <p v-else>&nbsp;</p> <!-- 빈칸으로 남김 -->

                                        <p class="category-heading">시나리오 요약</p>
                                        <p v-if="totalGameRecordsFiltered[currentPage]">{{
                                            totalGameRecordsFiltered[currentPage].total_summary }}</p>
                                        <p v-else>&nbsp;</p> <!-- 빈칸으로 남김 -->

                                        <p class="category-heading">{{ name }} 의 감정 분석</p>
                                        <p v-if="totalGameRecordsFiltered[currentPage]">{{
                                            totalGameRecordsFiltered[currentPage].emotion }}</p>
                                        <p v-else>&nbsp;</p> <!-- 빈칸으로 남김 -->

                                        <p class="category-heading">추천하는 영화</p>
                                        <p v-if="totalGameRecordsFiltered[currentPage]">{{
                                            totalGameRecordsFiltered[currentPage].recommend_movie }}</p>
                                        <p v-else>&nbsp;</p> <!-- 빈칸으로 남김 -->

                                        <p class="category-heading">이 영화를 추천하는 이유</p>
                                        <p v-if="totalGameRecordsFiltered[currentPage]">#{{
                                            totalGameRecordsFiltered[currentPage].recommend_movie_theme }}</p>
                                        <p v-else>&nbsp;</p> <!-- 빈칸으로 남김 -->

                                        <p v-if="totalGameRecordsFiltered[currentPage]">{{
                                            totalGameRecordsFiltered[currentPage].recommend_movie_reason }}</p>
                                        <p v-else>&nbsp;</p> <!-- 빈칸으로 남김 -->
                                    </div>
                                </div>
                            </div>

                            <!-- 전적 기록 -->
                            <div v-if="totalGameRecordsFiltered && totalGameRecordsFiltered[currentPage]"
                                v-for="(record, index) in totalGameRecordsFiltered[currentPage].history" :key="index"
                                class="container-8-game-info">
                                <div class="number-game-info" v-if="record.round > 1">{{ record.round - 1 }}</div>
                                <div class="sub-container-2-game-info" v-if="record.round > 1">
                                    <div class="container-9">
                                        <div class="sub-container-3">
                                            <img v-if="record.evaluation === '적절함'" class="selected-or-discarded"
                                                src="@/assets/icons/selected.png" alt="selected" />
                                            <img v-else class="selected-or-discarded" src="@/assets/icons/discarded.png"
                                                alt="discarded" />
                                        </div>
                                    </div>
                                    <div class="paragraph manrope-normal-mountain-mist-18px">
                                        <p class="category-heading">상황</p>
                                        <p>{{ record.situation }}</p>

                                        <p class="category-heading"> 당신의 대답</p>
                                        <p>{{ record.user_action || '없음' }}</p>

                                        <p class="category-heading">이유</p>
                                        <p>{{ record.reason || '없음' }}</p>
                                    </div>
                                </div>
                            </div>

                        </div>

                        <!-- 페이지 이동 버튼 -->
                        <div class="buttons-container-game-info">
                            <!-- 이전 페이지 버튼 -->
                            <button class="page-move-button-game-info" @click.prevent="currentPage = 0">
                                <img class="page-move-game-info" src="@/assets/icons/arrowarrowleft.png" alt="Button" />
                            </button>

                            <!-- 한 페이지 뒤로 가기 버튼 -->
                            <button class="page-move-button-game-info"
                                @click.prevent="currentPage === 0 ? currentPage = 0 : currentPage--">
                                <img class="page-move-game-info" src="@/assets/icons/arrowleft.png" alt="Button" />
                            </button>

                            <!-- 페이지 인디케이터 -->
                            <div class="indicators-container">
                                <p class="number-game-info-p">{{ currentPage + 1 }} / {{ totalGameRecordsFilteredPages +
                                    1
                                    }}</p>
                            </div>

                            <!-- 한 페이지 앞으로 가기 버튼 -->
                            <button class="page-move-button-game-info" @click.prevent="
                                currentPage === totalGameRecordsFilteredPages ? currentPage = totalGameRecordsFilteredPages : currentPage++
                                ">
                                <img class="page-move-game-info" src="@/assets/icons/arrowright.png" alt="Button" />
                            </button>

                            <!-- 마지막 페이지로 이동 버튼 -->
                            <button class="page-move-button-game-info" @click.prevent="
                                currentPage = totalGameRecordsFilteredPages
                                ">
                                <img class="page-move-game-info" src="@/assets/icons/arrowarrowright.png"
                                    alt="Button" />
                            </button>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/accountStore';
import { useRouter } from 'vue-router'
import { ref, onMounted, computed } from 'vue'
import axios from 'axios';

const store = useAccountStore()
const router = useRouter()
const isUpdatePasswordModalOpen = ref(false)
const isUpdateUserInfoModalOpen = ref(false)
const isGameInfoSearchModalOpen = ref(false)
const currentPassword = ref(null)
const newPassword1 = ref(null)
const newPassword2 = ref(null)
const BASE_URL = 'http://127.0.0.1:8000'
const newNickname = ref(null)
const newAge = ref(null)
const newSex = ref(null)
const name = ref(null)
const age = ref(null)
const sex = ref(null)
const email = ref(null)
const avg_win_point = ref(null)
const avg_win_rate = ref(null)
const isDropdownOpen = ref(null)
const totalGameRecordsAll = ref([])
const totalGameRecordsAllPages = ref(0)
const totalGameRecordsFiltered = ref([])
const totalGameRecordsFilteredPages = ref(0)
const currentPage = ref(0)
const SelectedMovies = ref(null)
const lastFetchTime = ref(null)
const wins = ref(0)
const loss = ref(0)
const redStars = ref(0)
const halfStar = ref(0)
const grayStars = ref(0)
const playedMovies = ref(['All Movies'])

onMounted(() => {
    store.getUserInfo()
    email.value = store.userInfo.email
    name.value = store.userInfo.name
    sex.value = store.userInfo.sex
    age.value = store.userInfo.age
    avg_win_point.value = store.userInfo.avg_win_point
    document.addEventListener('click', handleClickOutside);
})

const computedGameRecords = computed(() => {
    if (!totalGameRecordsFiltered.value || shouldRefetchData.value) {
        fetchGameRecords()
    }
    return totalGameRecordsFiltered.value
})

const shouldRefetchData = computed(() => {
    return !lastFetchTime.value || (Date.now() - lastFetchTime.value > 5 * 60 * 1000)
})

const fetchGameRecords = () => {
    if (isGameInfoSearchModalOpen.value) {
        axios({
            method: "GET",
            url: `${BASE_URL}/gameApp/user_record/${store.userId}/`,
            headers: { "Authorization": `Token ${store.token}` },
        }).then((res) => {
            // console.log(res)
            // API 응답 데이터가 존재하는지 확인
            if (res.data && res.data.game_records) {
                totalGameRecordsAll.value = res.data.game_records;
                totalGameRecordsAllPages.value = totalGameRecordsAll.value.length - 1;
                lastFetchTime.value = Date.now();

                if (totalGameRecordsAll.value.length > 0) {
                    totalGameRecordsAll.value.forEach(record => {
                        playedMovies.value.push(record.movie.title);
                        const cleanHistory = removeEscapeCharacters(record.history);
                        const parsedHistory = parseStringToObjectArray(cleanHistory);
                        record.history = parsedHistory;

                        // 승패 계산
                        record.history.forEach(stage => {
                            // stage.evaluation이 존재할 때만 평가를 확인합니다.
                            if (stage.evaluation && stage.evaluation === '적절함') {
                                wins.value++;
                            } else {
                                loss.value++;
                            }
                        });
                    });

                    // 평균 승률 및 별 개수 계산
                    avg_win_point.value = `${wins.value} 채택 / ${loss.value} 폐기`;
                    avg_win_rate.value = Number(((wins.value / (wins.value + loss.value)) * 5).toFixed(1));
                    redStars.value = Math.floor(avg_win_rate.value);
                    halfStar.value = avg_win_rate.value % 1 >= 0.5 ? 1 : 0;
                    grayStars.value = 5 - redStars.value - halfStar.value;

                    // playedMovies 중복 제거

                    playedMovies.value = [...new Set(playedMovies.value)];

                    totalGameRecordsFiltered.value = totalGameRecordsAll.value;
                    totalGameRecordsFilteredPages.value = totalGameRecordsAllPages.value;
                    window.alert(`${store.userInfo.name}님의 전적을 가져왔습니다!`);
                } else {
                    window.alert(`${store.userInfo.name}님은 아직 게임을 플레이한적이 없습니다!`);
                }
            } else {
                window.alert('게임 기록을 가져오는 데 실패했습니다.');
            }
        }).catch(err => {
            window.alert('전적 검색에 실패했습니다.');
            console.log(err)
            isGameInfoSearchModalOpen.value = false;
        });
    }
}

const handleGameInfoSearchModal = () => {
    if (!isGameInfoSearchModalOpen.value && !isUpdateUserInfoModalOpen.value && !isUpdatePasswordModalOpen.value) {
        isGameInfoSearchModalOpen.value = true
    } else if (isGameInfoSearchModalOpen.value) {
        isGameInfoSearchModalOpen.value = false
    }
    computedGameRecords.value
}

// 드롭다운에서 영화를 선택하는 함수 : 필터링 기능
const selectMovie = (option) => {
    SelectedMovies.value = option

    if (option === "All Movies") {
        totalGameRecordsFiltered.value = totalGameRecordsAll.value;
        totalGameRecordsFilteredPages.value = totalGameRecordsAllPages.value;
    } else {
        totalGameRecordsFiltered.value = []
        totalGameRecordsFilteredPages.value = 0
        totalGameRecordsAll.value.forEach(record => {
            if (record.movie.title === option) {
                totalGameRecordsFiltered.value.push(record)
            }
        })
        totalGameRecordsFilteredPages.value = totalGameRecordsFiltered.value.length - 1
    }
}

// 메인 화면으로 돌아가주는 함수
const backToMain = () => {
    router.push({ name: 'main' })
}

// 비밀번호 변경해주는 함수
const updatePassword = () => {
    if (newPassword1.value != newPassword2.value) {
        window.alert("새로 입력한 두 비밀번호가 서로 일치하지 않습니다")
    }
    else {
        axios({
            method: 'POST',
            url: `${BASE_URL}/api/auth/password/change/`,
            data: {
                old_passowrd: currentPassword.value,
                new_password1: newPassword1.value,
                new_password2: newPassword1.value
            },
            headers: { "Authorization": `Token ${store.token}` }
        }).then(res => { window.alert("비밀번호가 성공적으로 변경되었습니다.") }).then(() => {
            closePasswordUpdateModal()
        }).catch(err => window.alert("비밀번호 변경에 문제가 생겼습니다"))
    }
}

// 유저 정보 변경해주는 함수
const updateUserInfo = () => {
    axios({
        method: 'PUT',
        url: `${BASE_URL}/accounts/update-info/`,
        data: {
            name: newNickname.value,
            age: newAge.value,
            sex: newSex.value
        },
        headers: {
            "Authorization": `Token ${store.token}`
        }
    }).then(res => {
        store.userInfo.name = res.data.user.name
        store.userInfo.age = res.data.user.age
        store.userInfo.sex = res.data.user.sex
        window.alert('성공적으로 유저 정보가 업데이트 되었습니다')
        return store.userInfo
    }).then((userInfo) => {
        name.value = userInfo.name
        age.value = userInfo.age
        sex.value = userInfo.sex
    }).then(() => {
        closeUpdateUserInfoModal()
    }).catch(err => window.alert('유저 정보 변경에 문제가 생겼습니다'))
}

// 이스케이프 문자를 제거합니다.
const removeEscapeCharacters = (inputString) => {
    if (typeof inputString !== 'string') {
        // console.warn("removeEscapeCharacters: Non-string input received", inputString);
        return inputString; // 문자열이 아니면 그대로 반환
    }
    return inputString
        .replace(/\\r/g, '')
        .replace(/\\n/g, '')
        .replace(/\\"/g, '"');
};


// 객체배열형태로 반환
const parseStringToObjectArray = (inputString) => {
    const objectsArray = [];
    let currentObject = '';
    let braceCount = 0; // 중괄호 개수 카운트

    for (let char of inputString) {
        if (char === '{') {
            if (braceCount === 0) {
                currentObject = '{'; // 새로운 객체 시작
            }
            braceCount++;
        } else if (char === '}') {
            braceCount--;
            currentObject += char;

            if (braceCount === 0) {
                // 객체가 완성되면 배열에 추가
                objectsArray.push(JSON.parse(currentObject)); // JSON.parse를 사용하여 객체로 변환
                currentObject = ''; // 현재 객체 초기화
            }
        } else if (braceCount > 0) {
            currentObject += char; // 현재 객체에 추가
        }
    }
    return objectsArray;
}

const closePasswordUpdateModal = () => {
    isUpdatePasswordModalOpen.value = false
    currentPassword.value = ""
    newPassword1.value = ""
    newPassword2.value = ""
}

const closeUpdateUserInfoModal = () => {
    isUpdateUserInfoModalOpen.value = false
    newNickname.value = null
    newAge.value = null
    newSex.value = null
}

const handleUpdatePasswordModal = () => {
    // 다른 모달(유저정보 변경, 전적검색 모달)들이 안띄워져 있다면 띄워
    if (!isGameInfoSearchModalOpen.value && !isUpdateUserInfoModalOpen.value) { isUpdatePasswordModalOpen.value = true }
}

const handleUpdateUserInfoModal = () => {
    // 다른 모달(비번변경, 전적검색 모달)들이 안띄워져 있다면 띄워
    if (!isGameInfoSearchModalOpen.value && !isUpdatePasswordModalOpen.value) { isUpdateUserInfoModalOpen.value = true }
}


//////////////////////////////////////////////////////////////////////////////////////////
// 드롭다운 외부 클릭 감지
const handleClickOutside = (event) => {
    const dropdown = document.querySelector('.dropdown');
    if (isDropdownOpen.value && dropdown && !dropdown.contains(event.target)) {
        isDropdownOpen.value = false; // 드롭다운 닫기
        newSex.value = null; // 성별 선택하지 않은 경우 null로 설정
    }
}

// 성별 선택
const selectSex = (sex) => {
    newSex.value = sex;
    isDropdownOpen.value = false; // 성별이 선택되었을 경우 드롭다운도 닫아버림
}
//////////////////////////////////////////////////////////////////////////////////////////

</script>



<style scoped>
@import url("https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css");
@import url("https://fonts.googleapis.com/css?family=Manrope:500,400,600");
/***************************************************/
/***************************************************/
/***************************************************/
/***************************************************/
/***************************************************/
/***************************************************/
/***************************************************/

.background-video {
    position: fixed;
    right: 0;
    bottom: 0;
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
    z-index: -1;
    object-fit: cover;
}

.star-rating {
    display: flex;
}

.star-class {
    width: 24px;
    /* 별의 크기를 조정 */
    height: auto;
}

.btn-group .dropdown-menu {
    background-color: var(--black10);
    min-width: 100%;
}

.btn-group .dropdown-item {
    color: var(--grey60);
    background-color: var(--black10);
}

.btn-group .dropdown-item:hover {
    background-color: var(--red45);
    color: #FFFFFF;
}

.btn-group .btn.btn-secondary {
    background-color: var(--black10);
    color: #FFFFFF;
}

.btn-group .btn-secondary:hover,
.btn-group .btn-secondary:focus,
.btn-group .btn-secondary:active {
    background-color: var(--red45) !important;
    color: #FFFFFF;
}

.button-sex-select {
    width: calc(100% - 38px);
    height: 24px;
    text-align: left;
    padding: 20px;
}

.dropdown-toggle-split {
    width: 38px;
}

.btn-group .dropdown-sex {
    text-align: center;
}

.btn-group .sex {
    /* 마우스 호버링에도 반응이 없어야함 */
    /* 단 disable은 사용하지 말 것 */
    pointer-events: none;
}

.btn-group {
    display: flex;
    justify-content: space-between;
    width: 100%;
    height: 100%;
}






.dropdown-menu {
    background-color: var(--black10);
}

.dropdown-item {
    color: var(--grey60);
    background-color: var(--black10);
}

.dropdown-item:hover {
    background-color: var(--red45);
    color: #FFFFFF;
}

.dropdown-divider {
    border-top: 1px solid var(--black15);
    margin: 0;
}


.dropdown .btn-secondary:hover,
.dropdown .btn-secondary:focus,
.dropdown .btn-secondary:active {
    background-color: var(--red45);
}

.div-wrapper {
    background-color: var(--black10);
    display: flex;
    flex-direction: row;
    justify-content: center;
    width: 100%;
}

.div-wrapper .div {
    background-color: var(--black10);
    width: 1440px;
    height: 1024px;
    position: relative;
}

.div-wrapper .button {
    display: flex;
    width: 86px;
    height: 86px;
    align-items: flex-start;
    gap: 10px;
    padding: 10px;
    position: absolute;
    top: 50px;
    left: 50px;
    background-color: var(--grey60);
    border-radius: 6px;
    border: 1px solid;
    border-color: var(--black10);
}

.div-wrapper .skip-previous-filled {
    position: relative;
    width: 66px;
    height: 66px;
}

.div-wrapper .overlap-group {
    position: absolute;
    width: 416px;
    height: 820px;
    top: 164px;
    left: 50px;
    border-radius: 10px;
}

.overlap-group-game-info {
    position: relative;
    width: 100%;
    height: 100%;
    border-radius: 10px;
}

.div-wrapper .sub-container {
    display: flex;
    flex-direction: column;
    width: 416px;
    height: 820px;
    align-items: flex-start;
    gap: 24px;
    padding: 40px;
    position: absolute;
    top: 0;
    left: 0;
    background-color: var(--black06);
    border-radius: 10px;
    border: 1px solid;
    border-color: var(--black15);
}

.div-wrapper .container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
    position: relative;
    align-self: stretch;
    width: 100%;
    flex: 0 0 auto;
}

.div-wrapper .heading-wrapper {
    display: flex;
    align-items: center;
    gap: 2px;
    position: relative;
    align-self: stretch;
    width: 100%;
    flex: 0 0 auto;
}

.div-wrapper .heading {
    flex: 1;
    margin-top: -1.00px;
    font-weight: 500;
    color: var(--grey60);
    font-size: 24px;
    line-height: 36px;
    position: relative;
    font-family: "Manrope", Helvetica;
    letter-spacing: 0;
}

.div-wrapper .sub-container-2 {
    display: flex;
    width: 82px;
    align-items: center;
    gap: 2px;
    position: relative;
    flex: 0 0 auto;
}

.sub-container-2-game-info {
    align-items: flex-start;
    display: flex;
    flex: 1;
    flex-direction: column;
    flex-grow: 1;
    gap: 14px;
    position: relative;
}

.div-wrapper .text-wrapper {
    position: relative;
    flex: 1;
    margin-top: -1.00px;
    font-family: "Manrope", Helvetica;
    font-weight: 500;
    color: var(--grey60);
    font-size: 16px;
    letter-spacing: 0;
    line-height: 24px;
}

.div-wrapper .container-wrapper {
    display: flex;
    flex-wrap: wrap;
    width: 82px;
    align-items: flex-start;
    gap: 10px 10px;
    position: relative;
    flex: 0 0 auto;
}

.div-wrapper .container-2 {
    display: inline-flex;
    align-items: flex-start;
    gap: 10px;
    padding: 6px 12px;
    position: relative;
    flex: 0 0 auto;
    background-color: var(--black10);
    border-radius: 6px;
    border: 1px solid;
    border-color: var(--abbey);
}

.div-wrapper .text {
    position: relative;
    width: fit-content;
    margin-top: -1.00px;
    font-family: "Manrope", Helvetica;
    font-weight: 500;
    color: #ffffff;
    font-size: 14px;
    letter-spacing: 0;
    line-height: 21px;
    white-space: nowrap;
}

.div-wrapper .container-3 {
    display: inline-flex;
    align-items: flex-start;
    gap: 10px;
    padding: 6px 12px;
    position: relative;
    flex: 0 0 auto;
    margin-right: -94.00px;
    background-color: var(--black10);
    border-radius: 6px;
    border: 1px solid;
    border-color: var(--abbey);
}

.div-wrapper .container-4 {
    display: flex;
    flex-direction: column;
    width: 147px;
    align-items: flex-start;
    gap: 10px;
    position: relative;
    flex: 0 0 auto;
}

.div-wrapper .sub-container-3 {
    display: flex;
    align-items: center;
    gap: 4px;
    position: relative;
    align-self: stretch;
    width: 100%;
    flex: 0 0 auto;
}

.div-wrapper .icon {
    position: relative;
    width: 20px;
    height: 20px;
}

.div-wrapper .sub-container-4 {
    display: flex;
    width: 147px;
    align-items: flex-start;
    gap: 16px;
    position: relative;
    flex: 0 0 auto;
}

.div-wrapper .container-5 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 4px;
    padding: 14px;
    position: relative;
    flex: 1;
    flex-grow: 1;
    background-color: var(--black10);
    border-radius: 8px;
    border: 1px solid;
    border-color: var(--abbey);
}

.div-wrapper .heading-2 {
    width: fit-content;
    margin-top: -1.00px;
    font-weight: 600;
    color: #ffffff;
    font-size: 16px;
    line-height: 24px;
    white-space: nowrap;
    position: relative;
    font-family: "Manrope", Helvetica;
    letter-spacing: 0;
}

.div-wrapper .sub-container-5 {
    display: inline-flex;
    align-items: center;
    gap: 2px;
    position: relative;
    flex: 0 0 auto;
}

.div-wrapper .container-6 {
    display: inline-flex;
    align-items: flex-start;
    gap: 1px;
    position: relative;
    flex: 0 0 auto;
}

.div-wrapper .shape {
    position: relative;
    width: 17.12px;
    height: 16.28px;
}

.div-wrapper .img {
    position: relative;
    flex: 0 0 auto;
}

.div-wrapper .button-wrapper {
    display: flex;
    align-items: center;
    gap: 70px;
    position: relative;
    align-self: stretch;
    width: 100%;
    flex: 0 0 auto;
}

.div-wrapper .button-2 {
    all: unset;
    box-sizing: border-box;
    display: flex;
    width: 336px;
    align-items: flex-start;
    gap: 10px;
    padding: 18px 24px;
    position: relative;
    background-color: var(--red45);
    border-radius: 8px;
}

.div-wrapper .text-2 {
    position: relative;
    width: 284px;
    height: 27px;
    margin-top: -1.00px;
    font-family: "Manrope", Helvetica;
    font-weight: 600;
    color: var(--absolutewhite);
    font-size: 18px;
    text-align: center;
    letter-spacing: 0;
    line-height: 27px;
    white-space: nowrap;
}

.div-wrapper .button-3 {
    all: unset;
    box-sizing: border-box;
    display: flex;
    width: 93px;
    height: 49px;
    align-items: flex-start;
    gap: 10px;
    padding: 10px;
    position: absolute;
    top: 526px;
    left: 283px;
    background-color: var(--grey60);
    border-radius: 6px;
    border: 1px solid;
    border-color: var(--black10);
    transform: rotate(-180.00deg);
}

.div-wrapper .text-wrapper-2 {
    position: relative;
    width: fit-content;
    margin-top: -1.00px;
    margin-right: -1.00px;
    transform: rotate(180.00deg);
    font-family: "Manrope", Helvetica;
    font-weight: 500;
    color: #ffffff;
    font-size: 20px;
    letter-spacing: 0;
    line-height: 30px;
    white-space: nowrap;
}

.div-wrapper .overlap {
    position: absolute;
    width: 921px;
    height: 960px;
    top: 32px;
    left: 491px;
}

.div-wrapper .container-7 {
    display: flex;
    flex-direction: column;
    width: 917px;
    height: 960px;
    align-items: flex-start;
    gap: 30px;
    padding: 50px;
    position: absolute;
    top: 0;
    left: 4px;
    background-color: var(--black06);
    border-radius: 12px;
    border: 1px solid;
    border-color: var(--black15);
}

.number-game-info {
    color: var(--grey60);
    font-family: var(--font-family-manrope);
    font-size: 30px;
    font-weight: 600;
    letter-spacing: 0;
    line-height: 45px;
    position: relative;
    width: 60px;
    text-align: center;
}

.number-game-info-summary {
    color: var(--grey60);
    font-family: var(--font-family-manrope);
    font-size: 30px;
    font-weight: 600;
    letter-spacing: 0;
    line-height: 45px;
    position: relative;
    width: 60px;
    text-align: center;
}

.container-7-game-info {
    align-items: flex-start;
    background-color: var(--black06);
    border: 1px solid;
    border-color: var(--black15);
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    /* gap: 30px; */
    height: 100%;
    /* left: 4px; */
    padding: 50px;
    top: 0;
    width: 100%;
}

.div-wrapper .sub-container-6 {
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
    align-self: stretch;
    width: 100%;
    flex: 0 0 auto;
}

.div-wrapper .text-container {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    position: relative;
    flex: 0 0 auto;
    color: var(--grey60)
}

.game-result {
    font-family: var(--font-family-manrope);
    letter-spacing: 0;
    position: relative;
    color: var(--grey60);
    font-size: var(--font-size-xl);
    font-weight: 600;
    line-height: 36px;
    margin-top: -1.00px;
    white-space: nowrap;
    width: fit-content;
    margin: 0px;
}

.div-wrapper .heading-3 {
    width: fit-content;
    margin-top: -1.00px;
    font-weight: 600;
    color: #ffffff;
    font-size: 24px;
    line-height: 36px;
    white-space: nowrap;
    position: relative;
    font-family: "Manrope", Helvetica;
    letter-spacing: 0;
}

.div-wrapper .button-4 {
    all: unset;
    box-sizing: border-box;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 14px 16px;
    position: relative;
    flex: 0 0 auto;
    background-color: var(--black10);
    border-radius: 8px;
    border: 1px solid;
    border-color: var(--black15);
}

.div-wrapper .text-3 {
    position: relative;
    width: fit-content;
    font-family: "Manrope", Helvetica;
    font-weight: 500;
    color: #ffffff;
    font-size: 18px;
    letter-spacing: 0;
    line-height: 27.5px;
    white-space: nowrap;
}

.div-wrapper .button-5 {
    position: relative;
    width: 30px;
    height: 30px;
}

.button-5-game-info {
    height: 30px;
    position: relative;
    width: 30px;
}

.div-wrapper .sub-container-7 {
    display: flex;
    flex-direction: column;
    height: 728px;
    align-items: flex-start;
    position: relative;
    align-self: stretch;
    width: 100%;
}

.div-wrapper .container-8 {
    display: flex;
    align-items: center;
    gap: 20px;
    padding: 20px 0px;
    position: relative;
    align-self: stretch;
    width: 100%;
    flex: 0 0 auto;
    border-top-width: 1px;
    border-top-style: solid;
    border-bottom-width: 1px;
    border-bottom-style: solid;
    border-color: var(--black15);
}

.container-8-game-info {
    align-items: center;
    align-self: stretch;
    border-bottom-style: solid;
    border-bottom-width: 1px;
    border-color: var(--black15);
    border-top-style: solid;
    border-top-width: 1px;
    display: flex;
    flex: 0 0 auto;
    gap: 20px;
    padding: 20px 0px;
    position: relative;
    width: 100%;
}

.container-8-game-info-summarize {
    /* align-items: center; */
    align-self: stretch;
    border-bottom-style: solid;
    border-bottom-width: 1px;
    border-color: var(--black15);
    border-top-style: solid;
    border-top-width: 1px;
    display: flex;
    flex-direction: column;
    flex: 0 0 auto;
    gap: 20px;
    padding-top: 20px;
    padding-bottom: 20px;
    padding-left: 20px;
    position: relative;
    width: 100%;
}

.div-wrapper .number {
    position: relative;
    width: 60px;
    font-family: "Manrope", Helvetica;
    font-weight: 600;
    color: var(--grey60);
    font-size: 30px;
    letter-spacing: 0;
    line-height: 45px;
}

.div-wrapper .sub-container-8 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 14px;
    position: relative;
    flex: 1;
    flex-grow: 1;
}

.div-wrapper .container-9 {
    display: inline-flex;
    align-items: center;
    position: relative;
    flex: 0 0 auto;
}

.div-wrapper .heading-4 {
    width: 659px;
    font-weight: 600;
    color: #ffffff;
    font-size: 20px;
    line-height: 30px;
    position: relative;
    font-family: "Manrope", Helvetica;
    letter-spacing: 0;
}

.div-wrapper .sub-container-9 {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 8px 10px;
    position: relative;
    flex: 0 0 auto;
    background-color: var(--black10);
    border-radius: 8px;
    border: 1px solid;
    border-color: var(--black15);
}

.sub-container-9-game-info {
    align-self: stretch;
    width: 100%;
    display: flex;
    align-items: center;
    position: relative;
    /* background-color: var(--black10); */
    justify-content: space-between;
    border-color: var(--black15);
}

.sub-container-10 {
    margin-top: 30px;
    align-items: flex-start;
    align-self: stretch;
    display: flex;
    flex-direction: column;
    height: 728px;
    position: relative;
    width: 100%;
    overflow-y: auto;
    /* 세로 스크롤 추가 */
    max-height: 728px;
    /*최대 높이를 기존 높이와 동일하게 설정*/
}

.div-wrapper .close {
    position: relative;
    width: 24px;
    height: 24px;
}

.div-wrapper .text-4 {
    position: relative;
    width: fit-content;
    margin-top: -1.00px;
    font-family: "Manrope", Helvetica;
    font-weight: 500;
    color: var(--grey60);
    font-size: 16px;
    letter-spacing: 0;
    line-height: 24px;
    white-space: nowrap;
}

.div-wrapper .paragraph {
    position: relative;
    align-self: stretch;
    font-family: "Manrope", Helvetica;
    font-weight: 400;
    color: var(--grey60);
    font-size: 18px;
    letter-spacing: 0;
    line-height: 27px;
}

.div-wrapper .span {
    font-family: "Manrope", Helvetica;
    font-weight: 400;
    color: var(--grey60);
    font-size: 18px;
    letter-spacing: 0;
    line-height: 27px;
}

.div-wrapper .text-wrapper-3 {
    font-weight: 700;
}

.div-wrapper .container-10 {
    display: flex;
    align-items: center;
    gap: 20px;
    padding: 20px 0px;
    position: relative;
    align-self: stretch;
    width: 100%;
    flex: 0 0 auto;
    border-bottom-width: 1px;
    border-bottom-style: solid;
    border-color: var(--black15);
}

.div-wrapper .container-11 {
    display: flex;
    align-items: center;
    position: relative;
    align-self: stretch;
    width: 100%;
    flex: 0 0 auto;
}

.div-wrapper .heading-5 {
    flex: 1;
    font-weight: 600;
    color: #ffffff;
    font-size: 20px;
    line-height: 30px;
    position: relative;
    font-family: "Manrope", Helvetica;
    letter-spacing: 0;
}

.div-wrapper .buttons-container {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    position: absolute;
    top: 893px;
    left: 482px;
}

.game-info-with-button {
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.buttons-container-game-info {
    display: flex;
    align-items: center;
    justify-content: center;
    position: absolute;
    /* 절대 위치 지정 */
    bottom: 0;
    /* 컨테이너의 하단에 위치 */
    left: 50%;
    /* 수평 중앙 정렬을 위한 설정 */
    transform: translateX(-50%);
    /* 중앙 정렬을 위한 변환 */
    width: 100%;
    /* 필요에 따라 전체 너비 사용 */
    padding: 10px;
    /*선택 사항: 위아래 패딩 추가*/
    gap: 25px;
    /* margin-top: ; */
}

.selected-or-discarded {
    width: 80px;
    height: 40px;
}

.div-wrapper .button-6 {
    all: unset;
    box-sizing: border-box;
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 14px;
    position: relative;
    flex: 0 0 auto;
    background-color: var(--black10);
    border-radius: 100px;
    border: 1px solid;
    border-color: var(--black15);
}

.page-move-button-game-info {
    border: 2px solid transparent;
    background-color: transparent;
    transition: border-color 0.3s ease;
    /* width: 40px;
    버튼의 크기를 고정
    height: 40px;
    버튼의 크기를 고정 */
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0;
}

.page-move-button-game-info:hover {
    border-color: var(--red45);
}

.page-move-game-info {
    flex: 0 0 auto;
    position: relative;
    width: 52px;
    height: 52px;
}

.div-wrapper .text-wrapper-4 {
    position: relative;
    width: fit-content;
    margin-top: -1.00px;
    font-family: "Manrope", Helvetica;
    font-weight: 400;
    color: #ffffff;
    font-size: 14px;
    letter-spacing: 0;
    line-height: 21px;
    white-space: nowrap;
}

.number-game-info-p {
    margin: 0px;
    color: var(--grey60);
    font-family: var(--font-family-manrope);
    font-size: 30px;
    font-weight: 600;
    letter-spacing: 0;
    line-height: 45px;
    position: relative;
    text-align: center;
}

.category-heading {
    color: var(--absolutewhite);
    font-size: var(--font-size-m);
    font-weight: 600;
    line-height: 30px;
    width: 659px;
    font-family: var(--font-family-manrope);
    letter-spacing: 0;
    position: relative;
    margin-bottom: 5px;
}

.div-wrapper .indicators-container {
    display: flex;
    width: 81px;
    align-items: flex-start;
    gap: 3px;
    position: relative;
}

.div-wrapper .shape-2 {
    position: relative;
    width: 23px;
    height: 4px;
    background-color: var(--red45);
    border-radius: 100px;
}

.div-wrapper .shape-3 {
    position: relative;
    flex: 1;
    flex-grow: 1;
    height: 4px;
    background-color: var(--black20);
    border-radius: 100px;
}

.div-wrapper .buttons-container-2 {
    display: inline-flex;
    align-items: center;
    gap: 30px;
    padding: 10px 40px;
    position: absolute;
    top: 877px;
    left: 0;
    background-color: var(--black06);
    border-radius: 12px;
    overflow: hidden;
    border: 4px solid;
    border-color: var(--black12);
}

.div-wrapper .button-7 {
    all: unset;
    box-sizing: border-box;
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 14px 24px;
    position: relative;
    flex: 0 0 auto;
    background-color: var(--black10);
    border-radius: 8px;
    border: 1px solid;
    border-color: var(--black10);
}

.div-wrapper .text-5 {
    position: relative;
    width: fit-content;
    margin-top: -1.00px;
    font-family: "Manrope", Helvetica;
    font-weight: 500;
    color: var(--absolutewhite);
    font-size: 18px;
    letter-spacing: 0;
    line-height: 27px;
    white-space: nowrap;
}

.div-wrapper .text-button {
    position: relative;
    width: fit-content;
    font-family: "Manrope", Helvetica;
    font-weight: 400;
    color: var(--grey75);
    font-size: 18px;
    letter-spacing: 0;
    line-height: 27px;
    white-space: nowrap;
}

.div-wrapper .rectangle {
    position: absolute;
    width: 5px;
    height: 175px;
    top: 138px;
    left: 888px;
    background-color: var(--grey60);
    border-radius: 10px;
}









/***************************************************/
/***************************************************/
/***************************************************/
/***************************************************/
/***************************************************/
/***************************************************/
/***************************************************/

.dropdown-options {
    width: 200px;
    height: 68px;
    position: absolute;
    background-color: var(--black10);
    /* color: white; */
    color: var(--black15);
    border: 1px solid;
    z-index: 10;
}

.option {
    /* padding: 10px; */
    color: var(--black15);
    border-color: white;
    /* border-color: var(--black15); */
    width: 50px;
    height: 34px;
    cursor: pointer;
}

.input-box {
    border: 0px;
    padding: 0px;
    background-color: var(--black10);
}

.cancel {
    border: 0px;
    padding: 0px;
    color: var(--absolutewhite);
    text-align: center;
    flex: 1;
    font-family: var(--font-family-manrope);
    font-size: var(--font-size-m);
    font-weight: 400;
    letter-spacing: 0;
    line-height: 27px;
    margin-top: -1.00px;
    margin-bottom: 0px;
}

.option-common {

    border: 0px;
    padding: 0px;
    color: var(--absolutewhite);
    text-align: center;
    flex: 1;
    font-family: var(--font-family-manrope);
    font-size: var(--font-size-m);
    font-weight: 400;
    letter-spacing: 0;
    line-height: 27px;
    /* margin-top: -1.00px; */
    margin-bottom: 0px;
    position: relative;
}

.greybutton-common {
    align-items: center;
    align-self: stretch;
    background-color: var(--black15);
    border: 1px solid;
    border-color: var(--grey60);
    border-radius: 8px;
    display: flex;
    flex: 0 0 auto;
    gap: 77px;
    overflow: hidden;
    padding: 20px;
    position: relative;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0px 0px;
    width: 362px;
    height: 68px;
    transition: all 0.3s ease;
}

.game-record-button:hover {
    background-color: var(--grey60);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.cancel-button {
    align-items: center;
    align-self: stretch;
    background-color: var(--black10);
    border: 2px solid var(--grey60);
    border-radius: 8px;
    display: flex;
    flex: 0 0 auto;
    gap: 77px;
    overflow: hidden;
    padding: 20px;
    position: relative;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0px 0px;
    width: 314;
    height: 69px;
    transition: all 0.3s ease;
}

.cancel-button:hover {
    background-color: var(--grey60);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.game-record-button {
    align-items: center;
    align-self: stretch;
    background-color: var(--black10);
    border: 2px solid var(--grey60);
    border-radius: 8px;
    display: flex;
    flex: 0 0 auto;
    overflow: hidden;
    padding: 20px;
    width: 100%;
    display: flex;
    padding: 0px 0px;
    height: 77px;
    transition: all 0.3s ease;
}


.red-button-common {
    align-items: center;
    align-self: stretch;
    background-color: var(--black10);
    border: 2px solid var(--red45);
    border-radius: 8px;
    display: flex;
    flex: 0 0 auto;
    gap: 77px;
    overflow: hidden;
    padding: 20px;
    position: relative;
    width: 100%;
    transition: all 0.3s ease;
}

.red-button-common:hover {
    background-color: var(--red45);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.container-center-horizontal--profile {
    display: flex;
    flex-direction: row;
    justify-content: center;
    pointer-events: none;
    width: 100%;
    align-items: center;
    /* margin-top: 200px; */
    margin: auto;
}

.container-center-horizontal--profile>* {
    flex-shrink: 0;
    pointer-events: auto;
}

.screen a {
    display: contents;
    text-decoration: none;
}

.valign-text-middle {
    display: flex;
    flex-direction: column;
    justify-content: center;
}

* {
    box-sizing: border-box;
}

.flex-col {
    align-items: flex-start;
    display: flex;
    flex-direction: column;
    gap: 28px;
    margin-top: 10px;
    min-height: 934px;
    width: 416px;
}

.previous {
    height: 66px;
    position: relative;
    width: 66px;
}

.sub-container-2 {

    background-color: var(--black06);
    border: 1px solid;
    border-color: var(--black15);
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    gap: 24px;
    padding: 40px;
    width: 416px;
    height: 944px;
}

.container {
    align-items: flex-start;
    align-self: stretch;
    display: flex;
    flex: 0 0 auto;
    flex-direction: column;
    gap: 10px;
    position: relative;
    width: 100%;
    padding: 0px
}

.sub-container-3 {
    align-items: center;
    align-self: stretch;
    display: flex;
    flex: 0 0 auto;
    gap: 2px;
    position: relative;
    width: 100%;
}

.sub-container {
    align-items: center;
    display: flex;
    flex: 0 0 auto;
    gap: 2px;
    position: relative;
    width: 82px;
}

.sub-container-1 {
    align-items: flex-start;
    display: flex;
    flex: 0 0 auto;
    flex-wrap: wrap;
    gap: 10px 10px;
    position: relative;
    width: 82px;
}

.container-1 {
    align-items: flex-start;
    background-color: var(--black10);
    border: 1px solid;
    border-color: var(--abbey);
    border-radius: 6px;
    display: inline-flex;
    flex: 0 0 auto;
    gap: 10px;
    padding: 6px 12px;
    position: relative;
}

.sub-container-4 {
    align-items: center;
    align-self: stretch;
    display: flex;
    flex: 0 0 auto;
    gap: 4px;
    position: relative;
    width: 100%;
}

.sub-container-5 {
    align-items: flex-start;
    display: flex;
    flex: 0 0 auto;
    gap: 16px;
    position: relative;
    width: 147px;
}

.sub-container-6 {
    align-items: center;
    display: inline-flex;
    flex: 0 0 auto;
    gap: 2px;
    position: relative;
}

.container-7 {
    align-items: flex-start;
    display: inline-flex;
    flex: 0 0 auto;
    gap: 1px;
    position: relative;
}

.star-class {
    height: 16px;
    position: relative;
    width: 16px;
    flex: 0 0 auto;
}

.avg-win-rate {
    /* margin-left: 10px; */
    display: flex;
    align-items: flex-end;
    /* 내부 요소를 아래쪽에 정렬 */
}

.container-2 {
    align-items: center;
    align-self: stretch;
    display: flex;
    flex: 0 0 auto;
    gap: 70px;
    position: relative;
    width: 100%;
}

.items-container {
    align-items: flex-start;
    align-self: stretch;
    display: flex;
    flex: 0 0 auto;
    gap: 50px;
    position: relative;
    width: 100%;
}

.input-field {
    align-items: center;
    align-self: stretch;
    background-color: var(--black10);
    border: 1px solid;
    border-color: var(--abbey);
    border-radius: 8px;
    display: flex;
    flex: 0 0 auto;
    gap: 77px;
    overflow: hidden;
    padding: 20px;
    position: relative;
    width: 100%;
}

.heading-4 {
    letter-spacing: 0;
    margin-top: -1.00px;
    position: relative;
}

.text-5 {
    letter-spacing: 0;
    line-height: 27px;
    margin-top: -1.00px;
    position: relative;
}

.record {
    align-content: center;
    background-color: transparent;
    /* background-color: var(--black10); */
    display: flex;
    gap: 74px;
    height: 1024px;
    padding: 40px 50px;
    width: 1440px;
}

.record .button-1 {
    align-items: flex-start;
    /* background-color: var(--grey60); */
    background-color: transparent;
    border: 1px solid;
    border-color: var(--black12);
    border-radius: 6px;
    display: flex;
    gap: 10px;
    height: 86px;
    padding: 10px;
    position: relative;
    width: 86px;
}

.button-1-game-info {
    align-items: center;
    background-color: var(--black10);
    border: 1px solid;
    border-color: var(--black15);
    border-radius: 100px;
    display: inline-flex;
    flex: 0 0 auto;
    gap: 10px;
    padding: 14px;
    position: relative;
}

.record .overlap-group {
    border-radius: 10px;
    height: 820px;
    position: relative;
    width: 416px;
}

.record .heading-2 {
    flex: 1;
    line-height: 36px;
}

.record .heading {
    flex: 1;
    letter-spacing: 0;
    line-height: 24px;
    margin-top: -1.00px;
    position: relative;
}

.record .text {
    margin-bottom: 0px;
    letter-spacing: 0;
    line-height: 21px;
    margin-top: -1.00px;
    position: relative;
    white-space: nowrap;
    width: fit-content;
}

.record .container-4 {
    align-items: flex-start;
    background-color: var(--black10);
    border: 1px solid;
    border-color: var(--abbey);
    border-radius: 6px;
    display: inline-flex;
    flex: 0 0 auto;
    gap: 10px;
    margin-right: -94.00px;
    padding: 6px 12px;
    position: relative;
}

.record .container-5 {
    align-items: flex-start;
    display: flex;
    flex: 0 0 auto;
    flex-direction: column;
    gap: 10px;
    position: relative;
    width: 147px;
}

.record .icon {
    height: 20px;
    position: relative;
    width: 20px;
}

.record .container-6 {
    align-items: flex-start;
    background-color: var(--black10);
    border: 1px solid;
    border-color: var(--abbey);
    border-radius: 8px;
    display: flex;
    flex: 1;
    flex-direction: column;
    flex-grow: 1;
    gap: 4px;
    padding: 14px;
    position: relative;
}

.record .heading-3 {
    line-height: 24px;
    white-space: nowrap;
    width: fit-content;
}

.record .button {
    align-items: flex-start;
    background-color: var(--red45);
    border-radius: 8px;
    display: flex;
    gap: 10px;
    padding: 18px 24px;
    position: relative;
    width: 336px;
}

.record .text-1 {
    height: 27px;
    text-align: center;
    white-space: nowrap;
    width: 284px;
}

.record .button-2 {
    align-items: flex-start;
    background-color: var(--grey60);
    border: 1px solid;
    border-color: var(--black12);
    border-radius: 6px;
    display: flex;
    gap: 10px;
    height: 49px;
    left: 283px;
    padding: 10px;
    position: absolute;
    top: 526px;
    transform: rotate(-180.00deg);
    width: 93px;
}

.record .text-2-1 {
    letter-spacing: 0;
    line-height: 30px;
    margin-right: -1.00px;
    margin-top: -1.00px;
    position: relative;
    transform: rotate(180.00deg);
    white-space: nowrap;
    width: fit-content;
}

.record .form {
    align-items: flex-start;
    background-color: var(--black06);
    border: 1px solid;
    border-color: var(--black15);
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    gap: 50px;
    height: 820px;
    margin-top: 124px;
    padding: 50px;
    position: relative;
    width: 416px;
}

.record .container-3 {
    align-items: flex-start;
    display: flex;
    flex: 1;
    flex-direction: column;
    flex-grow: 1;
    gap: 16px;
    position: relative;
}

.record .heading-1 {
    align-self: stretch;
    line-height: 27px;
}

.record .text-2 {
    flex: 1;
}

.record .button-3 {
    height: 24px;
    position: relative;
    width: 24px;
}

.record .button-4 {
    align-items: flex-start;
    background-color: var(--red45);
    border-radius: 8px;
    display: flex;
    gap: 10px;
    padding: 18px 24px;
    position: relative;
    width: 314px;
}

.btn.btn-secondary.dropdown-toggle.button-4-game-info {
    align-items: center;
    background-color: var(--black10);
    border: 2px solid var(--red45);
    border-radius: 8px;
    display: inline-flex;
    flex: 0 0 auto;
    gap: 4px;
    padding: 14px 16px;
    position: relative;
    height: 100%;
    transition: all 0.3s ease;
}

.btn.btn-secondary.dropdown-toggle.button-4-game-info:focus,
.btn.btn-secondary.dropdown-toggle.button-4-game-info:active,
.btn.btn-secondary.dropdown-toggle.button-4-game-info:hover {
    background-color: var(--red45);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.record .text-3 {
    height: 27px;
    text-align: center;
    white-space: nowrap;
    width: 266px;
}

.record .button-5 {
    align-items: flex-start;
    background-color: var(--grey60);
    border-radius: 8px;
    display: flex;
    gap: 10px;
    padding: 18px 24px;
    position: relative;
    width: 314px;
}

.record .text-4 {
    text-align: center;
    width: 266px;
}

.text-4-game-info {
    color: var(--absolutewhite);
    font-family: var(--font-family-manrope);
    font-size: var(--font-size-m);
    font-weight: 500;
    letter-spacing: 0;
    line-height: 27.5px;
    position: relative;
    white-space: nowrap;
    width: fit-content;
}

manrope-semi-bold-white-18px {
    color: var(--absolutewhite);
    font-family: var(--profile-font-family-manrope);
    font-size: var(--profile-font-size-m);
    font-style: normal;
    font-weight: 600;
}

.manrope-medium-mountain-mist-16px {
    color: var(--grey60);
    font-family: var(--profile-font-family-manrope);
    font-size: var(--profile-font-size-s);
    font-style: normal;
    font-weight: 500;
}

.manrope-medium-white-14px {
    color: var(--absolutewhite);
    font-family: var(--profile-font-family-manrope);
    font-size: var(--profile-font-size-xs);
    font-style: normal;
    font-weight: 500;
}

.avg-win-rate-class {
    color: var(--absolutewhite);
    font-family: var(--profile-font-family-manrope);
    font-size: 14px;
    font-style: normal;
    font-weight: 500;
}

.manrope-normal-mountain-mist-18px {
    color: var(--grey60);
    font-family: var(--profile-font-family-manrope);
    font-size: var(--profile-font-size-m);
    font-style: normal;
    font-weight: 400;
}

.manrope-medium-mountain-mist-18px {
    color: var(--grey60);
    font-family: var(--profile-font-family-manrope);
    font-size: var(--profile-font-size-m);
    font-style: normal;
    font-weight: 500;
}

.manrope-medium-mountain-mist-18px-option {
    color: var(--grey60);
    font-family: var(--profile-font-family-manrope);
    font-size: var(--profile-font-size-l);
    font-style: normal;
    font-weight: 500;
}

.manrope-medium-mountain-mist-24px {
    color: var(--grey60);
    font-family: var(--profile-font-family-manrope);
    font-size: var(--profile-font-size-xl);
    font-style: normal;
    font-weight: 500;
}

.manrope-semi-bold-white-16px {
    color: var(--absolutewhite);
    font-family: var(--profile-font-family-manrope);
    font-size: var(--profile-font-size-s);
    font-style: normal;
    font-weight: 600;
}

.manrope-medium-white-20px {
    color: var(--absolutewhite);
    font-family: var(--profile-font-family-manrope);
    font-size: var(--profile-font-size-l);
    font-style: normal;
    font-weight: 500;
}
</style>