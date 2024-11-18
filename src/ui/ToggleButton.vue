<template>
  <button class="toggle-button" :class="{active: isActive}" @click="$emit('toggle-event')">
    <template v-if="direction === 'left'">
      <span v-if="isActive"><i class="fa-solid fa-chevron-left"></i></span>
      <span v-else><i class="fa-solid fa-chevron-right"></i></span>
    </template>
    <template v-else-if="direction === 'right'">
      <span v-if="isActive"><i class="fa-solid fa-chevron-right"></i></span>
      <span v-else><i class="fa-solid fa-chevron-left"></i></span>
    </template>
    <template v-else-if="direction === 'top'">
      <span v-if="isActive"><i class="fa-solid fa-chevron-up"></i></span>
      <span v-else><i class="fa-solid fa-chevron-down"></i></span>
    </template>
    <template v-else>
      <span v-if="isActive"><i class="fa-solid fa-chevron-down"></i></span>
      <span v-else><i class="fa-solid fa-chevron-up"></i></span>
    </template>
  </button>
</template>

<script setup>
  defineProps(['isActive', 'direction'])
  defineEmits(['toggle-event'])
</script>

<style scoped>
  .toggle-button {
    background-color: #dddddd;
    color: #363536;
    cursor: pointer;
    font-size: 1.2rem;
    border-style: solid;
    border-color: #f78e09;
  }

  .toggle-button.active {
    background-color: #f78e09;
  }
</style>
