<template>
  <Sidebar position="left">
    <div id="companies-filters">
      <label id="favourite-checkbox">
        <input type="checkbox" v-model="favouriteChecked" />
        Favourite
      </label>
      <div id="companies-tags">
        <label v-for="tag in companiesTags">
          <input :id="tag.id" v-model="checkedTags" :value="tag.name" type="checkbox" />
          {{ tag.name }}
        </label>
      </div>
    </div>
  </Sidebar>
</template>

<script setup>
  import { computed, ref, watch } from "vue";
  import { companiesFilters, companiesTags } from "@/store.js";
  import { where } from "firebase/firestore";
  import Sidebar from "@/ui/Sidebar.vue";

  // Favourite handler
  const favouriteChecked = ref(true);
  const favouriteFilter = computed(() => {
    return favouriteChecked.value ? [where("favourite", "==", favouriteChecked)] : []
  });

  // Tag handler
  const checkedTags = ref([])
  const tagsFilter = computed(() => checkedTags.value.map(key => where(`tags.${key}`, "==", true)));

  // Apply filters
  companiesFilters.value = favouriteFilter.value.concat(tagsFilter.value)
  watch([favouriteChecked, tagsFilter], () => {
    companiesFilters.value = favouriteFilter.value.concat(tagsFilter.value)
  })
</script>

<style scoped>
  .sidebar-container {
    height: 100%;
  }
</style>
