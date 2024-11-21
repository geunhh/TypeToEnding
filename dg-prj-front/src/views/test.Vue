<template>
<div class="game-wrapper">
    <div class="round-header">
        <h1>Round {{ gamestore.game_round }}/5</h1>
        <div class="progress-bar">
            <div class="progress" :style="{ width: `${(gamestore.game_round / 5) * 100}%` }"></div>
        </div>
    </div>

    <div class="playgame-container">
        <div class="status-badge" :class="{ 'accepted': result.is_valid, 'rejected': !result.is_valid }">
            시나리오를
            <span>{{ result.is_valid ? '채택' : '폐기' }}</span>
            합니다
        </div>

        <div class="content-grid">
            <div class="scenario-card">
                <h3>플레이어의 시나리오</h3>
                <div class="card-content">
                    <p>{{ gamestore.user_action1 }}</p>
                </div>
            </div>

            <div class="evaluation-card">
                <h3>AI의 평가</h3>
                <div class="card-content">
                    <p>{{ result.reason }}</p>
                </div>
            </div>
        </div>

        <button class="next-button" @click="nextStage" :disabled="isLoading">
            {{ gamestore.game_round === 4 ? '결과 보기' : '다음 라운드' }}
        </button>
    </div>
</div>

</template>

<script setup>
import { useGameStore, useMovieStore } from '@/stores/counter';
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const moviestore = useMovieStore();
const gamestore = useGameStore();
const isLoading = ref(false);

const result = ref(router.options.history.state.result);

const nextStage = async () => {
    try {
        isLoading.value = true;
        gamestore.game_round++;

        if (gamestore.game_round > 4) {
            await router.push({ name: 'ResultPage' });
        } else {
            await router.push({
                name: 'loading',
                query: { next_problem: result.value.next_problem }
            });
        }
    } catch (error) {
        console.error('Navigation error:', error);
    } finally {
        isLoading.value = false;
    }
};
</script>

<style scoped>
.game-wrapper {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.round-header {
    text-align: center;
    margin-bottom: 30px;
}

.progress-bar {
    width: 100%;
    height: 8px;
    background: #2c2c2c;
    border-radius: 4px;
    overflow: hidden;
    margin-top: 10px;
}

.progress {
    height: 100%;
    background: red;
    transition: width 0.3s ease;
}

.status-badge {
    text-align: center;
    padding: 12px 24px;
    border-radius: 8px;
    font-weight: 600;
    margin: 20px auto;
    width: fit-content;
    background: #1a1a1a;
    color: white;
}

.status-badge.accepted span {
    color: #4CAF50;
}

.status-badge.rejected span {
    color: #f44336;
}

.content-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 40px;
    margin: 40px 0;
}

.scenario-card,
.evaluation-card {
    background: #1a1a1a;
    border-radius: 12px;
    padding: 20px;
    height: 500px;
    display: flex;
    flex-direction: column;
}

.card-content {
    flex: 1;
    overflow-y: auto;
    padding: 20px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 8px;
    margin-top: 15px;
}

h3 {
    color: white;
    margin: 0;
    padding-bottom: 15px;
    text-align: center;
    font-size: 1.2rem;
}

.next-button {
    display: block;
    margin: 30px auto;
    padding: 15px 40px;
    font-size: 1.1rem;
    font-weight: 600;
    background: red;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.next-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(255, 0, 0, 0.2);
}

.next-button:disabled {
    background: #666;
    cursor: not-allowed;
    transform: none;
    box-shadow: none;
}

@media (max-width: 768px) {
    .content-grid {
        grid-template-columns: 1fr;
    }

    .scenario-card,
    .evaluation-card {
        height: 400px;
    }
}
</style>