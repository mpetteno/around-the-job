<template>
  <div class="sidebar-container">
    <div class="sidebar" v-show="isSidebarOpen">
      <slot></slot>
    </div>
    <ToggleButton :is-active="isSidebarOpen" :direction="position" @toggle-event="toggleSidebar"/>
  </div>
</template>

<script setup>
  defineProps(['position'])
  import ToggleButton from "@/ui/ToggleButton.vue";
  import { ref } from "vue";
  const isSidebarOpen = ref(false);
  const toggleSidebar = () => {
    isSidebarOpen.value = !isSidebarOpen.value;
  };
</script>

<style scoped>
  .sidebar-container {
    display: flex;
    position: fixed;
    z-index: 99999;
    align-items: center;
    top: 0;
    left: 0;
  }

  .sidebar {
    width: 250px;
    background-color: #f4f4f4;
    padding: 20px;
    box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
    transition: left 0.3s ease;
  }
</style>
