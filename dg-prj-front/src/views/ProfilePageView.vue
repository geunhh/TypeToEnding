<template>
    <div class="container-center-horizontal--profile">
        <div class="record screen">
            <div class="flex-col">
                <button class="button-1" @click.prevent="backToMain">
                    <img class="previous" src="@/assets/icons/previous.png" alt="previous" />
                </button>
                <div class="overlap-group">
                    <div class="sub-container-2">
                        <div class="container">
                            <div class="sub-container-3">
                                <h1 class="heading-2 valign-text-middle heading-4 manrope-medium-mountain-mist-24px">
                                    {{ name }}’s Profile Page
                                </h1>
                            </div>
                        </div>
                        <div class="container">
                            <div class="sub-container">
                                <div class="heading manrope-medium-mountain-mist-16px">Nickname</div>
                            </div>
                            <div class="sub-container-1">
                                <div class="container-1">
                                    <div class="text manrope-medium-white-14px">{{ name }}</div>
                                </div>
                            </div>
                        </div>
                        <div class="container">
                            <div class="sub-container">
                                <div class="heading manrope-medium-mountain-mist-16px">Age</div>
                            </div>
                            <div class="sub-container-1">
                                <div class="container-1">
                                    <p class="text manrope-medium-white-14px">{{ age !== null ? age : "?" }}</p>
                                </div>
                            </div>
                        </div>
                        <div class="container">
                            <div class="sub-container">
                                <div class="heading manrope-medium-mountain-mist-16px">Sex</div>
                            </div>
                            <div class="sub-container-1">
                                <div class="container-1">
                                    <div class="text manrope-medium-white-14px">{{ sex !== null ? sex : "?" }}</div>
                                </div>
                            </div>
                        </div>
                        <div class="container">
                            <div class="sub-container">
                                <div class="heading manrope-medium-mountain-mist-16px">Email</div>
                            </div>
                            <div class="sub-container-1">
                                <div class="container-4">
                                    <div class="text manrope-medium-white-14px">{{ email }}</div>
                                </div>
                            </div>
                        </div>
                        <div class="container-5">
                            <div class="sub-container-4">
                                <div class="heading manrope-medium-mountain-mist-16px">Win rate</div>
                            </div>
                            <div class="sub-container-5">
                                <div class="container-6">
                                    <div class="heading-3 heading-4 manrope-semi-bold-white-16px">{{ avg_win_point !==
                                        null ? avg_win_point : "0W 0L" }}</div>
                                    <div class="sub-container-6">
                                        <div class="container-7">
                                            <img class="star" src="@/assets/icons/star.png" alt="star" />
                                            <img class="star" src="@/assets/icons/star.png" alt="star" />
                                            <img class="star" src="@/assets/icons/star.png" alt="star" />
                                            <img class="star" src="@/assets/icons/star.png" alt="star" />
                                            <img class="half-star" src="@/assets/icons/half-star.png" alt="half-star" />
                                        </div>
                                        <div class="text manrope-medium-white-14px">4.5</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="container-2">
                            <button class="red-button-common" @click.prevent="handleUpdatePasswordModal">
                                <p class="option-common">Change Password</p>
                            </button>
                        </div>
                        <div class="container-2">
                            <button class="red-button-common" @click.prevent="handleUpdateUserInfoModal">
                                <p class="option-common">Update Profile</p>
                            </button>
                        </div>
                    </div>
                    <button class="game-record-button" @click.prevent="handleGameInfoSearchModal">
                        <p class="cancel">{{ !isGameInfoSearchModalOpen ? "Open Record" : "Close Record" }}</p>
                    </button>
                </div>
            </div>

            <!-- 드롭다운이 겁나 짜쳐요.... -->
            <form class="form" v-if="isUpdateUserInfoModalOpen && !isUpdatePasswordModalOpen">
                <div class="items-container">
                    <div class="container-3">
                        <div class="heading-1 heading-4 manrope-semi-bold-white-18px">Nickname</div>
                        <div class="input-field">
                            <input class="text-2 text-5 input-box manrope-normal-mountain-mist-18px" type="text"
                                v-model="newNickname" :placeholder="store.userInfo.name">
                        </div>
                    </div>
                </div>
                <div class="items-container">
                    <div class="container-3">
                        <div class="heading-1 heading-4 manrope-semi-bold-white-18px">Age</div>
                        <div class="input-field">
                            <input class="text-2 text-5 input-box manrope-medium-mountain-mist-18px" v-model="newAge"
                                :placeholder="store.userInfo.age">
                        </div>
                    </div>
                </div>

                <div class="items-container">
                    <div class="container-3">
                        <div class="heading-1 heading-4 manrope-semi-bold-white-18px">Sex</div>
                        <div class="input-field ">
                            <div class="text-2 text-5  manrope-medium-mountain-mist-18px" @click="toggleDropdown">
                                {{ newSex === 'M' ? '남자' : newSex === 'F' ? '여자' : '성별 선택' }}
                            </div>
                            <img class="button-3 dropdown" src="@/assets/icons/drop-down.png" alt="Button"
                                @click="toggleDropdown" style="margin-left: 8px; cursor: pointer;" />
                            <div v-if="isDropdownOpen" class="dropdown-options">
                                <div @click="selectSex('M')" class="option manrope-medium-mountain-mist-18px-option">남자
                                </div>
                                <div @click="selectSex('F')" class="option manrope-medium-mountain-mist-18px-option">여자
                                </div>
                            </div>
                        </div>
                    </div>
                </div>




                <!-- <div class="items-container">
                    <div class="container-3">
                        <div class="heading-1 heading-4 manrope-semi-bold-white-18px">Sex</div>
                        <div class="input-field">

                            <div class="text-2 text-5 manrope-medium-mountain-mist-18px">Male</div>

                            <img class="button-3" src="@/assets/icons/drop-down.png" alt="Button" />

                        </div>
                    </div>
                </div> -->

                <div class="container-2">
                    <button class="red-button-common" @click.prevent="updateUserInfo">
                        <p class="option-common">Update</p>
                    </button>
                </div>
                <div class="container-2">
                    <button class="cancel-button" @click.prevent="closeUpdateUserInfoModal">
                        <p class="cancel">Cancel</p>
                    </button>
                </div>
            </form>
            <!-- 여기까지가 유저정보 모달 -->
            <!-- 아래부터는 비밀번호 모달 -->
            <form class="form" v-if="isUpdatePasswordModalOpen && !isUpdateUserInfoModalOpen">
                <div class="items-container">
                    <div class="container-3">
                        <div class="heading-1 heading-4 manrope-semi-bold-white-18px">Old Password</div>
                        <div class="input-field">
                            <input type="password" class="input-box text-2 text-5 manrope-normal-mountain-mist-18px"
                                placeholder="Enter your old password" v-model="currentPassword">
                        </div>
                    </div>
                </div>
                <div class="items-container">
                    <div class="container-3">
                        <div class="heading-1 heading-4 manrope-semi-bold-white-18px">New Password</div>
                        <div class="input-field">
                            <input type="password" class="input-box text-2 text-5 manrope-normal-mountain-mist-18px"
                                placeholder="Enter your new password" v-model="newPassword1">
                        </div>
                    </div>
                </div>
                <div class="items-container">
                    <div class="container-3">
                        <div class="heading-1 heading-4 manrope-semi-bold-white-18px">Confirm</div>
                        <div class="input-field">
                            <input type="password" class="input-box text-2 text-5 manrope-normal-mountain-mist-18px"
                                placeholder="Confirm your new password" v-model="newPassword2">
                        </div>
                    </div>
                </div>
                <div class="container-2">
                    <button class="red-button-common" @click.prevent="updatePassword">
                        <p class="option-common manrope-semi-bold-white-18px">Update</p>
                    </button>
                </div>
                <div class="container-2">
                    <button class="cancel-button" @click.prevent="isUpdatePasswordModalOpen = false">
                        <p class="cancel manrope-semi-bold-white-18px">Cancel</p>
                    </button>
                </div>
            </form>

            <!-- 여기까지가 비밀번호 모달 -->
            <!-- 아래부터는 전적검색 모달 -->



            <div class="overlap-group-game-info" v-if="isGameInfoSearchModalOpen">
                <div class="container-7-game-info">
                    <div class="sub-container-9-game-info">
                        <div class="text-container">
                            <div class="heading-3 heading-6">최종 결과</div>
                        </div>
                        <div class="button-4">
                            <!-- <div class="text-4">All Movies</div>
                            <img class="button-5" src="#" alt="Button" /> -->
                        </div>
                    </div>
                    <div class="sub-container-10">
                        <div v-for="(record) in totalGameRecordsAll[0].history" :key=index class="container-8-game-info">
                            <div class="number">{{ record.round }}</div>
                            <div class="sub-container-2-game-info">
                                <div class="container-9">
                                    <div class="sub-container-3">
                                        <img class="close" src="#" alt="close" />
                                        <div class="text-2 manrope-medium-mountain-mist-16px">폐기</div>
                                    </div>
                                </div>
                                <p class="paragraph manrope-normal-mountain-mist-18px">
                                    <span class="manrope-normal-mountain-mist-18px">상황<br /></span>
                                    <span class="span-1">{{ record.situation }}<br /></span>
                                    <span class="manrope-normal-mountain-mist-18px">
                                        <br />
                                        유저의 행동
                                        <br />
                                        {{ record.user_action || '없음' }}
                                        <br />
                                        <br />
                                    </span>
                                    <span class="span-1">평가 결과 : {{ record.evaluation }}
                                        <br />
                                        이유: {{ record.reason || '없음' }}
                                    </span>
                                </p>
                            </div>
                        </div>
                    </div>
                    <div class="buttons-container-game-info">
                        <div class="button-1-game-info">
                            <div class="text-3">맨앞</div>
                        </div>
                        <img class="button-6" src="#" alt="Button" />
                        <div class="indicators-container">
                            <div class="shape-3"></div>
                            <div class="shape-1"></div>
                            <div class="shape-1"></div>
                            <div class="shape-1"></div>
                        </div>
                        <img class="button-7" src="#" alt="Button" />
                        <div class="button-1-game-info">
                            <div class="text-3">맨뒤</div>
                        </div>
                    </div>

                    <!-- <div class="buttons-container-1">
                        <div class="button-8">
                            <div class="text-5">자세히 보기</div>
                        </div>
                        <div class="text-button">요약해서 보기</div>
                    </div> -->
                </div>
                <div class="rectangle-521"></div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/accountStore';
import { useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
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
const isDropdownOpen = ref(null)
const totalGameRecordsAll = ref(null)
const totalGameRecordsFiltered = ref(null)
const totalGameRecordsAllPages = ref(null)
const totalGameRecordsFilteredPages = ref(null)
const currentPage = ref(0)

onMounted(() => {
    store.getUserInfo()
    email.value = store.userInfo.email
    name.value = store.userInfo.name
    sex.value = store.userInfo.sex
    age.value = store.userInfo.age
    avg_win_point.value = store.userInfo.avg_win_point
    document.addEventListener('click', handleClickOutside);
})

// 메인 화면으로 돌아가주는 함수
const backToMain = () => {
    router.push({ name: 'main' })
}

// 전적 검색 모달 열어주는 함수
const gameInfoSearch = () => {
    isGameInfoSearchModalOpen.value = true
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
        console.log(res.data.user)
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
    return inputString
        .replace(/\\r/g, '') // \r 제거
        .replace(/\\n/g, '') // \n 제거
        .replace(/\\"/g, '"'); // 이스케이프된 따옴표를 원래의 따옴표로 변환
}

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



// 실질적으로 전적을 DB에서 가져오는 함수
const getGameRecord = () => {
    // 모달이 열릴 때만
    // axios로 전적 받아와라
    if (isGameInfoSearchModalOpen.value) {
        axios({
            method: "GET",
            // url: `${BASE_URL}/gameApp/user_record/6/`,
            url: `${BASE_URL}/gameApp/user_record/5/`,
            // url: `${BASE_URL}/gameApp/user_record/${store.userId}/`,
            headers: { "Authorization": `Token ${store.token}` },
        }).then((res) => {
            // console.log(res.data.game_records)
            totalGameRecordsAll.value = res.data.game_records
            totalGameRecordsAllPages.value = res.data.game_records.length
        }).then(() => {
            if (!(totalGameRecordsAll.value === null && totalGameRecordsAll.value === undefined)) {
                if (!totalGameRecordsAllPages.value) { window.alert(`${store.userInfo.name}님은 아직 게임을 플레이한적이 없습니다!`) }
                else {
                    window.alert(`${store.userInfo.name}님의 전적을 가져왔습니다!`)
                    // 여기서 히스토리 파싱 + 정리하자
                    totalGameRecordsAll.value.forEach(record => {
                        const cleanHistory = removeEscapeCharacters(record.history)
                        const parsedHistory = parseStringToObjectArray(cleanHistory)
                        record.history = parsedHistory
                        console.log(record.history);


                        // console.log(record.movie);
                        // console.log(record.total_summary);
                        // console.log(record.total_score);
                        // console.log(record.recommend_movie);
                        // console.log(record.recommend_movie_reason);
                        // console.log(record.recommend_movie_theme);
                        // console.log(record.emotion);

                    });



                    // console.log(totalGameRecordsAll.value[0]);
                }
            }

        }).catch(err => {
            window.alert('전적 검색에 실패했습니다.')
            isGameInfoSearchModalOpen.value = false // 전적 가져오는 데에 실패하면 모달 닫아버리셈
        })
    }
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

// 전적 모달 띄워주는 함수
const handleGameInfoSearchModal = () => {
    // 다른 모달(비번변경, 전적검색 모달)들이 안띄워져 있다면 띄워

    // 이 버튼은 특별하게 전적보기 버튼으로만 열고 닫기가 됨
    if (!isGameInfoSearchModalOpen.value && !isUpdateUserInfoModalOpen.value && !isUpdatePasswordModalOpen.value) {
        isGameInfoSearchModalOpen.value = true
    } else if (isGameInfoSearchModalOpen.value) {
        isGameInfoSearchModalOpen.value = false
    }
    getGameRecord()
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

// 드롭다운 열기/닫기
const toggleDropdown = () => {
    isDropdownOpen.value = !isDropdownOpen.value;
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

.div-wrapper {
    background-color: #1a1a1a;
    display: flex;
    flex-direction: row;
    justify-content: center;
    width: 100%;
}

.div-wrapper .div {
    background-color: #1a1a1a;
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
    background-color: #808080;
    border-radius: 6px;
    border: 1px solid;
    border-color: #1e1e1e;
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
    background-color: #0f0f0f;
    border-radius: 10px;
    border: 1px solid;
    border-color: var(--black-15);
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
    color: var(--grey-60);
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
    color: var(--grey-60);
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
    background-color: #1a1a1a;
    border-radius: 6px;
    border: 1px solid;
    border-color: #4e4e4e;
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
    background-color: #1a1a1a;
    border-radius: 6px;
    border: 1px solid;
    border-color: #4e4e4e;
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
    background-color: var(--black-08);
    border-radius: 8px;
    border: 1px solid;
    border-color: #4e4e4e;
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
    background-color: var(--red-45);
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
    background-color: #808080;
    border-radius: 6px;
    border: 1px solid;
    border-color: #1e1e1e;
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
    background-color: var(--black-06);
    border-radius: 12px;
    border: 1px solid;
    border-color: var(--black-15);
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
    position: absolute;
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
    background-color: var(--black-08);
    border-radius: 8px;
    border: 1px solid;
    border-color: var(--black-15);
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
    border-color: var(--black-15);
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

.div-wrapper .number {
    position: relative;
    width: 60px;
    font-family: "Manrope", Helvetica;
    font-weight: 600;
    color: var(--grey-60);
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
    background-color: var(--black-08);
    border-radius: 8px;
    border: 1px solid;
    border-color: var(--black-15);
}

.sub-container-9-game-info {
    align-self: stretch;
    width: 100%;
    display: flex;
    align-items: center;
    position: relative;
    flex: 0 0 auto;
    background-color: var(--black-08);
    justify-content: space-between;
    border-color: var(--black-15);
    margin-bottom: 30px;
}

.sub-container-10 {
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
    color: var(--grey-60);
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
    color: var(--grey-60);
    font-size: 18px;
    letter-spacing: 0;
    line-height: 27px;
}

.div-wrapper .span {
    font-family: "Manrope", Helvetica;
    font-weight: 400;
    color: #999999;
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
    border-color: var(--black-15);
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
    padding-bottom: 20px;
    /*선택 사항: 위아래 패딩 추가*/
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
    background-color: var(--black-08);
    border-radius: 100px;
    border: 1px solid;
    border-color: var(--black-15);
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
    background-color: var(--red-45);
    border-radius: 100px;
}

.div-wrapper .shape-3 {
    position: relative;
    flex: 1;
    flex-grow: 1;
    height: 4px;
    background-color: var(--black-20);
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
    background-color: var(--black-06);
    border-radius: 12px;
    overflow: hidden;
    border: 4px solid;
    border-color: var(--black-12);
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
    background-color: var(--black-10);
    border-radius: 8px;
    border: 1px solid;
    border-color: var(--black-10);
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
    color: var(--grey-75);
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
    background-color: #d9d9d947;
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
    background-color: var(--black08);
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
    position: relative;
    background-color: var(--grey60);
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
    background-color: var(--red45);
}

.grey-button-common {
    align-items: center;
    align-self: stretch;
    background-color: var(--grey60);
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
}

.cancel-button {
    align-items: center;
    align-self: stretch;
    background-color: var(--grey60);
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
    width: 314;
    height: 69px;
}

.game-record-button {
    align-items: center;
    align-self: stretch;
    background-color: var(--grey60);
    border: 1px solid;
    border-color: var(--grey60);
    border-radius: 8px;
    display: flex;
    flex: 0 0 auto;
    gap: 77px;
    overflow: hidden;
    padding: 20px;
    position: absolute;
    top: 505px;
    left: 216px;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0px 0px;
    width: 159px;
    height: 77px;
}


.red-button-common {
    align-items: center;
    align-self: stretch;
    background-color: var(--red45);
    border: 1px solid;
    border-color: var(--red45);
    border-radius: 8px;
    display: flex;
    flex: 0 0 auto;
    gap: 77px;
    overflow: hidden;
    padding: 20px;
    position: relative;
    width: 100%;
}

.container-center-horizontal--profile {
    display: flex;
    flex-direction: row;
    justify-content: center;
    pointer-events: none;
    width: 100%;
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
    align-items: flex-start;
    background-color: var(--black06);
    border: 1px solid;
    border-color: var(--black15);
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    gap: 24px;
    height: 820px;
    left: 0;
    padding: 40px;
    position: absolute;
    top: 0;
    width: 416px;
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

.star {
    height: 16.28px;
    position: relative;
    width: 17.12px;
}

.half-star {
    flex: 0 0 auto;
    position: relative;
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
    background-color: var(--black08);
    border: 1px solid;
    border-color: var(--black15);
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
    align-items: flex-start;
    background-color: var(--black10);
    display: flex;
    gap: 74px;
    height: 1024px;
    padding: 40px 50px;
    width: 1440px;
}

.record .button-1 {
    align-items: flex-start;
    background-color: var(--grey60);
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
    background-color: var(--black08);
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
    background-color: var(--black08);
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