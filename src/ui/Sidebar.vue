<template>
  <div class="sidebar-container">
    <div class="sidebar" v-show="isSidebarOpen">
      <slot></slot>
    </div>
    <ToggleButton :is-active="isSidebarOpen" :direction="position" @toggle-event="isSidebarOpen = !isSidebarOpen"/>
  </div>
</template>

<script setup>
  defineProps(['position'])
  import ToggleButton from "@/ui/ToggleButton.vue";
  import { ref } from "vue";
  const isSidebarOpen = ref(false);
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
    background-color: #f4f4f4;
    padding: 20px;
    box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
    transition: left 0.3s ease;
    flex-shrink: 1000;
  }

  @media (max-width: 768px) {
    .sidebar {
      height: 100vh;
      overflow-y: auto;
    }

    .favourite-checkbox {
      margin: 10px;
    }

    #tags {
      flex-direction: column;
    }

    .reset-btn {
      width: 100%;
      text-align: center;
    }
  }
</style>
