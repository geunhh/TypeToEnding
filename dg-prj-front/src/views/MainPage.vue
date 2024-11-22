<template>
    <div class="container-center-horizontal--main" @click="howToPlayHandler">
        <div class="main screen">
            <!-- title -->
            <h1 class="title">Type to Ending</h1>
            <div class="overlap-group-container">
                <div class="overlap-group">
                    <!-- 여기에는 주요 요소들 -->
                    <!--how to play modal-->
                    <div class="black-bg show-how-to-play" v-if="modalStore.isHowToPlayModalOpen"
                        @click="howToPlayHandler">
                        <howToPlay class="how-to-play-modal" />
                    </div>

                    <!-- 방 입장을 위한 모달 >> 개발 보류 -->
                    <div class="card" v-if="isEnterRoomModalOpen" @click="closeEnterRoomModal">
                        <div class="text-container">
                            <div class="heading valign-text-middle">영화관 코드를 입력해주세요</div>
                        </div>
                        <div class="buttons-container">
                            <div class="button-4">
                                <div class="text-3 valign-text-middle">3F7D</div>
                            </div>
                            <div class="button-5">
                                <div class="text-4">확인</div>
                            </div>
                        </div>
                    </div>

                    <!-- 로그인 이전 -->
                    <form class="form" v-if="!accountStore.token">
                        <div class="items-container">
                            <div class="container">
                                <div class="heading manrope-semi-bold-white-18px">E-mail</div>
                                <div class="input-field">
                                    <input v-model="email" type="text" class="text email-pw-input"
                                        placeholder="Enter your email">
                                </div>
                            </div>
                        </div>
                        <div class="items-container">
                            <div class="container">
                                <div class="heading manrope-semi-bold-white-18px">Password</div>
                                <div class="input-field">
                                    <input v-model="password" type="password" class="text email-pw-input"
                                        placeholder="Enter your password">
                                </div>
                            </div>
                        </div>
                        <div class="items-container">
                            <div class="container">
                                <button @click.prevent="loginFunc" class="red-button-common">
                                    <input type="submit" class="option-common" value="log in">
                                </button>
                            </div>
                        </div>
                        <!-- 버튼 누르면 다른 페이지로 감 -->
                        <!-- <div class="items-container">
                            <div class="container">
                                <RouterLink :to="{ name: 'SignUpView' }">
                                    <button class="grey-button-common">
                                        <span class="sign-up">Sign Up</span>
                                    </button>
                                </RouterLink>
                            </div>
                        </div> -->
                        <div class="items-container">
                            <div class="container">
                                <button class="grey-button-common" @click.prevent="toggleSignUpModal">
                                    <span class="sign-up">{{ isSignUpModalOpen ? "Close Form" : "Sign Up" }}</span>
                                </button>
                            </div>
                        </div>
                    </form>

                    <!-- 로그인 이후 -->
                    <div class="form" v-else>
                        <div class="items-container">
                            <div class="container">
                                <button @click.prevent="moveToProfilePage" class="red-button-common">
                                    <p style="padding: 0px 0px; margin: 0px" class="option-common">Profile</p>
                                </button>
                            </div>
                        </div>
                        <div class="items-container">
                            <div class="container">
                                <button @click.prevent="CreateRoom" class="red-button-common">
                                    <p style="padding: 0px 0px; margin: 0px" class="option-common">Create Room</p>
                                </button>
                            </div>
                        </div>
                        <div class="items-container">
                            <div class="container">
                                <button @click.prevent="isEnterRoomModalOpen = false" class="red-button-common">
                                    <p style="padding: 0px 0px; margin: 0px" class="option-common">Enter Room</p>
                                </button>
                            </div>
                        </div>
                        <div class="items-container">
                            <div class="container">
                                <button @click.prevent="logOutFunc" class="grey-button-common log-out-button">
                                    <p style="padding: 0px 0px; margin: 0px" class="log-out">Log Out</p>
                                </button>
                            </div>
                        </div>
                        <img class="generic-avatar" src="@/assets/icons/generic-avatar.png" alt="generic-avatar"
                            @click.prevent="moveToProfilePage">
                        <img class="add-circle" src="@/assets/icons/add-circle.png" alt="add-circle"
                            @click.prevent="CreateRoom">
                        <img class="forward" src="@/assets/icons/forward.png" alt="forward"
                            @click.prevent="isEnterRoomModalOpen = true">
                    </div>
                </div>
                <form class="form-1" v-if="!accountStore.token && isSignUpModalOpen">
                    <div class="items-container">
                        <div class="container">
                            <div class="input-field">
                                <input v-model.trim="newEmail" type="email" class="text email-pw-input"
                                    placeholder="Enter your email">
                            </div>
                        </div>
                    </div>
                    <div class="items-container">
                        <div class="container">
                            <div class="input-field">
                                <input v-model.trim="newNickname" type="text" class="text email-pw-input"
                                    placeholder="Enter your nickname">
                            </div>
                        </div>
                    </div>
                    <div class="items-container">
                        <div class="container">
                            <div class="input-field">
                                <input v-model.trim="newPassword1" type="password" class="text email-pw-input"
                                    placeholder="Enter your password">
                            </div>
                        </div>
                    </div>
                    <div class="items-container">
                        <div class="container">
                            <div class="input-field">
                                <input v-model.trim="newPassword2" type="password" class="text email-pw-input"
                                    placeholder="Confirm your password">
                            </div>
                        </div>
                    </div>
                    <div class="items-container">
                        <div class="container">
                            <button class="red-button-common" @click.prevent="signUpFunc">
                                <div class="option-common manrope-semi-bold-white-18px">Sign Up</div>
                            </button>
                        </div>
                    </div>
                </form>

                <!-- 공간차지용 더미 태그 : 삭제하지 말것 -->
                <div class="dummy-form" v-else>

                </div>






























                <!-- 얘 손좀 보자 -->
                <!-- 모달을 띄워주는 버튼 -->
                <div class="overlap-group-1">
                    <button class="button-2 button-3 modal-button">
                        <img class="icon modal-button" src="@/assets/icons/icon.png" alt="Icon" />
                        <div class="modal-button show-how-to-play text-2 valign-text-middle manrope-semi-bold-white-32px"
                            @click.prevent="howToPlayHandler">How to play</div>
                    </button>
                </div>

















            </div>
        </div>
    </div>
</template>

<script setup>
import howToPlay from '@/components/howToPlay.vue';
import { useAccountStore } from '@/stores/accountStore';
import { useModalStore } from '@/stores/modalStore';
import { useGameStore, useMovieStore, useUserStore } from '@/stores/counter';
import { ref, onMounted } from 'vue';
import { RouterLink, useRouter } from 'vue-router';
import { v4 as uuidv4 } from 'uuid'

const moviestore = useMovieStore()
const accountStore = useAccountStore()
const modalStore = useModalStore()
const gamesStore = useGameStore()

const router = useRouter()

const email = ref(null)
const password = ref(null)

const newEmail = ref(null)
const newPassword1 = ref(null)
const newPassword2 = ref(null)
const newNickname = ref(null)

const isEnterRoomModalOpen = ref(false)
const isSignUpModalOpen = ref(false)


// 초기 설정
onMounted(() => {
    moviestore.movie_name = null
    moviestore.description = null
    moviestore.context = null
    moviestore.poster_path = null
    moviestore.movieId = null
    modalStore.isHowToPlayModalOpen = false
    gamesStore.game_round = 0
    
    console.log(accountStore.token)
})

// 회원 가입폼에 입력한 정보 초기화하는 함수
const resetForm = () => {
    newEmail.value = ""
    newPassword1.value = ""
    newPassword2.value = ""
    newNickname.value = ""
}

// 프로필 페이지로 이동하는 함수
const moveToProfilePage = () => {
    router.push({
        name: 'ProfilePageView',
        params: { userId: accountStore.userId }
    })
}

// 로그인 함수
const loginFunc = function () {
    console.log(email.value)
    console.log(password.value)
    const payload = {
        email: email.value,
        password: password.value,
    }
    accountStore.logIn(payload)
}

// 로그아웃 함수
const logOutFunc = function () {
    accountStore.logOut()
}

// 회원 가입하는 함수
const signUpFunc = () => {
    const payload = {
        email: newEmail.value,
        password1: newPassword1.value,
        password2: newPassword2.value,
        name: newNickname.value,
    }
    accountStore.signUp(payload)
    resetForm()
}

// 방 생성 하는 함수
const CreateRoom = function () {
    // 방 번호가 랜덤으로 들어가야함. 이지만 나중에 해보자잇.

    const roomId = uuidv4()
    moviestore.roomId = roomId
    console.log(moviestore.roomId)
    router.push({ name: 'LoungeView', params: { roomId } })
}

// 방 입장 모달 닫기 >> 개발 보류
const closeEnterRoomModal = (event) => {
    if (event.target.classList.contains('card')) {
        isEnterRoomModalOpen.value = false;
    }
}

// 방 입장 모달 열기 >> 개발 보류
const enterRoomFunc = () => {
    isEnterRoomModalOpen.value = true
}

// 게임 설명 모달을 열어주는 함수
const howToPlayHandler = (event) => {
    const { target } = event;
    const { isHowToPlayModalOpen } = modalStore;

    const closeModalTargets = [
        'container-center-horizontal--main',
        'screen',
        'title',
        'black-bg'
    ];

    if (isHowToPlayModalOpen) {
        // 모달이 열려있다면
        if (closeModalTargets.some(targetClass => target.classList.contains(targetClass))) {
            // 닫을 수 있는 요소를 클릭했으면 모달 닫기
            modalStore.isHowToPlayModalOpen = false;
        } else {
            // 모달 내부 클릭 시 계속 열어둠
            modalStore.isHowToPlayModalOpen = true;
        }
    } else if (target.classList.contains('modal-button')) {
        // 모달이 닫혀있고, 모달 버튼을 클릭했으면 열어줘
        modalStore.isHowToPlayModalOpen = true;
    }
}

// 게임 설명 모달을 닫아주는 함수 >> 모달 외부 클릭하면 닫아짐
// 내가 의도한 것 : 모달 창 외부를 클릭 >> 흰 화면 바깥 어디를 클릭해도 닫아져야함
// 모달의 배경은 배경색상과 똑같음 >> 체감상 없다고 생각할 수 있음 >> 여기 클릭하면 닫아지는거 완료
// 그런데 제목은 보여야함 >> 제목에는 모달 배경이 안덮여있음 >> 따라서 "모달 배경"의 외부를 클릭해도 닫아져야함
// 그러느니 그냥 흰 모달창 외부 or X 버튼 클릭시 닫아버리자

// 대기실로 입장하는 함수
const moveToWaitingRoom = () => {
    router.push({
        name: 'WaitingRoomView',
        params: { roomCode: "3F7D" }
    })
}

// 회원 가입 폼을 열고 닫는 함수, sign up 버튼에 적용됨
const toggleSignUpModal = () => {
    resetForm()
    isSignUpModalOpen.value = !isSignUpModalOpen.value
}

</script>

<style scoped>
/* 장식용 cdn */
/* @import url("https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css"); */
/* @import url("https://fonts.googleapis.com/css?family=Inter:400|Inknut+Antiqua:400|Manrope:400,600"); */
/* The following line is used to measure usage of this code. You can remove it if you want. */
/* @import url("https://px.animaapp.com/673df13076e2d7568d4b0197.673df13076e2d7568d4b019a.vdlRvPB.hcp.png"); */


.button-2 {
    border: 0px;
    align-items: center;
    gap: 4px;
    height: 63px;
    left: 0;
    position: absolute;
    top: 19px;
    width: 280px;
}

.button-3 {
    background-color: var(--red45);
    border-radius: 8px;
    display: flex;
    padding: 18px 24px;
}


.howtoplay-container {
    border: 1px white solid;
    background-color: red;
    font-weight: 600;
    padding: 10px;
    height: fit-content;
    margin-top: 5%;
}

body {
    margin: 0
}

div {
    box-sizing: border-box;
}

.black-bg {
    width: 100%;
    height: 100%;
    background: #1a1a1a;
    position: fixed;
    top: 100;
    /* 화면의 최상단 */
    left: 0;
    /* 화면의 좌측 */
    padding: 20px;
    z-index: 1000;
    /* 다른 요소 위에 표시 */
}





/***************************************************/
/***************************************************/
/***************************************************/
/***************************************************/
/***************************************************/
/***************************************************/

.form-1 {
    align-items: flex-start;
    background-color: var(--black06);
    border: 1px solid;
    border-color: var(--black15);
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    gap: 50px;
    height: 621px;
    margin-left: 27px;
    padding: 50px;
    position: relative;
    width: 488px;
}

.dummy-form {
    align-items: flex-start;
    background-color: var(--eerie-black);



    display: flex;
    flex-direction: column;
    gap: 50px;
    height: 621px;
    margin-left: 27px;
    padding: 50px;
    position: relative;
    width: 488px;
}

.text-2 {
    height: 63px;
    letter-spacing: 0;
    line-height: 48px;
    margin-bottom: -17.00px;
    margin-right: -3.00px;
    margin-top: -19.00px;
    position: relative;
    text-align: center;
    width: 203px;
}

.manrope-semi-bold-white-32px {
    color: var(--absolutewhite);
    font-family: var(--font-family-manrope);
    font-size: var(--font-size-l);
    font-style: normal;
    font-weight: 600;
}

.buttons-container {
    align-items: flex-start;
    align-self: stretch;
    display: flex;
    flex: 0 0 auto;
    gap: 20px;
    position: relative;
    width: 100%;
}

.button-4 {
    align-items: center;
    background-color: var(--black08);
    border: 1px solid;
    border-color: var(--black15);
    border-radius: 8px;
    display: flex;
    gap: 10px;
    height: 59px;
    justify-content: center;
    padding: 0px 24px;
    position: relative;
    width: 328px;
}

.text-3 {
    color: var(--absolutewhite);
    font-family: var(--font-family-manrope);
    font-size: var(--font-size-xxxl);
    font-weight: 600;
    height: 60px;
    letter-spacing: 0;
    line-height: 60px;
    margin-left: -23.50px;
    margin-right: -23.50px;
    margin-top: -1.50px;
    position: relative;
    text-align: center;
    white-space: nowrap;
    width: 327px;
}

.button-5 {
    align-items: center;
    background-color: var(--red45);
    border-radius: 8px;
    display: flex;
    flex: 1;
    flex-grow: 1;
    gap: 10px;
    justify-content: center;
    padding: 18px 24px;
    position: relative;
}

.text-4 {
    color: var(--absolutewhite);
    font-family: var(--font-family-manrope);
    font-size: 15px;
    font-weight: 600;
    letter-spacing: 0;
    line-height: 22.5px;
    margin-left: -6.00px;
    margin-right: -6.00px;
    margin-top: -1.00px;
    position: relative;
    white-space: nowrap;
    width: fit-content;
}

.valign-text-middle {
    display: flex;
    flex-direction: column;
    justify-content: center;
}


.text-container {
    align-items: flex-start;
    align-self: stretch;
    display: flex;
    flex: 0 0 auto;
    flex-direction: column;
    gap: 16px;
    position: relative;
    width: 100%;
}


.card {
    align-items: flex-start;
    background-color: var(--black10);
    border: 1px solid;
    border-color: var(--black15);
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    gap: 50px;
    left: 466px;
    padding: 50px;
    position: absolute;
    top: 158px;
    width: 512px;
}

.generic-avatar {
    height: 45px;
    left: 90px;
    position: absolute;
    top: 62px;
    width: 45px;
}

.add-circle {
    height: 45px;
    left: 90px;
    position: absolute;
    top: 182px;
    width: 45px;
}

.forward {
    height: 45px;
    left: 90px;
    position: absolute;
    top: 301px;
    width: 45px;
}

.screen a {
    display: contents;
    text-decoration: none;
}

.container-center-horizontal--main {
    display: flex;
    flex-direction: row;
    justify-content: center;
    width: 100%;
}

.container-center-horizontal>* {
    flex-shrink: 0;
}

* {
    box-sizing: border-box;
}


/* screen - main */

.main {
    align-items: flex-start;
    background-color: var(--eerie-black);
    display: flex;
    flex-direction: column;
    gap: 10px;
    height: 1024px;
    padding: 29px 52px;
    width: 1440px;
    min-width: 1311px;
}

.main .title {
    align-self: center;
    color: var(--absolutewhite);
    font-family: var(--font-family-inknut_antiqua);
    font-size: var(--font-size-xxl);
    font-weight: 400;
    letter-spacing: 0;
    line-height: normal;
    margin-top: 87px;
    min-height: 248px;
    min-width: 816px;
    text-shadow: 0px 4px 4px #00000040;
}

.main .overlap-group-container {
    align-items: flex-start;
    display: flex;
    min-width: 1311px;
}

.main .overlap-group {
    border-radius: 12px;
    height: 621px;
    position: relative;
    width: 488px;
}

.main .id {
    color: var(--eerie-black);
    font-family: var(--font-family-inter);
    font-size: var(--font-size-xl);
    font-weight: 400;
    left: 38px;
    letter-spacing: 0;
    line-height: normal;
    position: absolute;
    top: 167px;
}

.main .pw {
    color: var(--eerie-black);
    font-family: var(--font-family-inter);
    font-size: var(--font-size-l);
    font-weight: 400;
    left: 38px;
    letter-spacing: 0;
    line-height: normal;
    position: absolute;
    top: 241px;
    width: 60px;
}

.main .remember-me {
    color: var(--eerie-black);
    font-family: var(--font-family-inter);
    font-size: var(--font-size-s);
    font-weight: 400;
    left: 52px;
    letter-spacing: 0;
    line-height: normal;
    position: absolute;
    top: 306px;
}

.main .form {
    align-items: flex-start;
    background-color: var(--black06);
    border: 1px solid;
    border-color: var(--black15);
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    gap: 50px;
    height: 621px;
    left: 0;
    padding: 50px;
    position: absolute;
    top: 0;
    width: 488px;
}

.main .items-container {
    align-items: flex-start;
    align-self: stretch;
    display: flex;
    flex: 0 0 auto;
    gap: 50px;
    position: relative;
    width: 100%;
}

.main .container {
    align-items: flex-start;
    display: flex;
    flex: 1;
    flex-direction: column;
    flex-grow: 1;
    gap: 16px;
    position: relative;
}

.main .heading {
    align-self: stretch;
    letter-spacing: 0;
    line-height: 27px;
    margin-top: -1.00px;
    position: relative;
}

.main .input-field {
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

.main .text {
    color: var(--grey60);
    flex: 1;
    font-family: var(--font-family-manrope);
    font-size: var(--font-size-m);
    font-weight: 400;
    letter-spacing: 0;
    line-height: 27px;
    margin-top: -1.00px;
    position: relative;
}



.email-pw-input {
    z-index: 1000;
    border: 0px;
    padding: 0px;
}



.main .container-1 {
    align-items: center;
    align-self: stretch;
    display: flex;
    flex: 0 0 auto;
    gap: 70px;
    position: relative;
    width: 100%;
}

.main .button {
    align-items: flex-start;
    background-color: var(--red45);
    border-radius: 8px;
    display: flex;
    gap: 10px;
    padding: 18px 24px;
    position: relative;
    width: 400px;
}



.main .overlap-group-1 {
    height: 82px;
    margin-left: 28px;
    margin-top: 78.0px;
    position: relative;
    width: 280px;
}

.main .icon-media-play {
    height: 27px;
    left: 253px;
    position: absolute;
    top: 0;
    width: 27px;
}


.main .icon {
    height: 28px;
    margin-bottom: -0.50px;
    margin-top: -0.50px;
    position: relative;
    width: 28px;
}





.manrope-semi-bold-white-18px {
    color: var(--absolutewhite);
    font-family: var(--font-family-manrope);
    font-size: var(--font-size-m);
    font-style: normal;
    font-weight: 600;
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
    margin-top: -1.00px;
    position: relative;
    background-color: var(--red45);
}

.log-out {
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
}

.sign-up {
    margin: 0;
    /* 기본 마진 제거 추가 */
    text-align: center;
    /* 텍스트 중앙 정렬 추가 */
    border: 0px;
    padding: 0px;
    color: var(--absolutewhite);
    flex: 1;
    font-family: var(--font-family-manrope);
    font-size: var(--font-size-m);
    font-weight: 400;
    letter-spacing: 0;
    line-height: 27px;
    margin-top: -1.00px;
    position: relative;
    background-color: var(--grey60);
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

.how-to-play-button-common {
    display: flex;
    /* Flexbox 사용 */
    align-items: center;
    /* 수직 중앙 정렬 */
    background-color: var(--red45);
    /* 버튼 배경색 */
    border: none;
    /* 기본 테두리 제거 */
    border-radius: 8px;
    /* 둥근 모서리 */
    padding: 10px 20px;
    /* 상하 패딩 10px, 좌우 패딩 20px */
    cursor: pointer;
    /* 커서 포인터 변경 */
}

.show-how-to-play {
    /* 아이콘과 텍스트 간격 */
    white-space: nowrap;
    /* 텍스트 줄 바꿈 방지 */
}

.log-out-button {
    margin-top: 81px;
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

/***************************************************/
</style>