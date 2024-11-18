<template>
  <Sidebar position="top">
    <h1>Menu</h1>
  </Sidebar>
</template>

<script setup>
  import Sidebar from "@/ui/Sidebar.vue";
</script>

<style scoped>
  .sidebar-container {
    width: 100%;
    flex-direction: column;
  }

  .sidebar-container >>> .sidebar {
    border-radius: 0 0 12px 12px;
  }

  .sidebar-container >>> .toggle-button {
    width: 56px;
    height: 24px;
    border-radius: 0 0 12px 12px;
    border-width: 0 1px 1px 1px;
  }
</style>
