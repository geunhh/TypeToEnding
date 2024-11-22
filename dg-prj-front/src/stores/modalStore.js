import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useModalStore = defineStore('modal', () => {
    let isHowToPlayModalOpen = ref(false)

    return {isHowToPlayModalOpen}
})