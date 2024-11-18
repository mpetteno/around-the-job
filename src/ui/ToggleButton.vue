<template>
  <button class="toggle-button" @click="$emit('toggle-event')">
    <template v-if="direction === 'left'">
      <span v-if="isActive">←</span>
      <span v-else>→</span>
    </template>
    <template v-else-if="direction === 'right'">
      <span v-if="isActive">→</span>
      <span v-else>←</span>
    </template>
    <template v-else-if="direction === 'top'">
      <span v-if="isActive">↑</span>
      <span v-else>↓</span>
    </template>
    <template v-else>
      <span v-if="isActive">↓</span>
      <span v-else>↑</span>
    </template>
  </button>
</template>

<script setup>
  defineProps(['isActive', 'direction'])
  defineEmits(['toggle-event'])
</script>

<style scoped>
  .toggle-button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px;
    cursor: pointer;
    font-size: 1.2rem;
    height: 48px;
  }
</style>
