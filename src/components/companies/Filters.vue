<template>
  <Sidebar position="left">
    <label class="favourite-checkbox" :class="{checked: favouriteChecked}">
      <input type="checkbox" v-model="favouriteChecked" v-show="false"/>
      <i class="fa-heart" :class="favouriteChecked ? 'fa-solid': 'fa-regular'"></i>
    </label>
    <div id="tags">
      <label v-for="tag in companiesTags" class="btn tag" :class="{checked: checkedTags.includes(tag.name)}">
        <input :id="tag.id" v-model="checkedTags" :value="tag.name" type="checkbox" v-show="false"/>
        {{ tag.name }}
      </label>
    </div>
    <button class="btn reset-btn" :class="{disabled: checkedTags.length === 0}" @click="checkedTags = []">Reset</button>
  </Sidebar>
</template>

<script setup>
  import Sidebar from "@/ui/Sidebar.vue";
  import { computed, ref, watch } from "vue";
  import { collection, query, where } from "firebase/firestore";
  import { useCollection, useFirestore } from "vuefire";
  import { companies } from '@/store.js'

  // Get collections
  const db = useFirestore();
  const companiesTags = useCollection(collection(db, "companies_tags"))
  const companiesCol = collection(db, "companies");
  const companiesFilters = ref([null]);
  const companiesQuery = computed(() => query(companiesCol, ...companiesFilters.value));
  useCollection(companiesQuery, { target: companies })

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
    max-width: 60%;
  }

  .sidebar-container >>> .sidebar {
    border-radius: 0 12px 12px 0;
  }

  .sidebar-container >>> .toggle-button {
    height: 56px;
    width: 24px;
    border-radius: 0 24px 24px 0;
    border-width: 1px 1px 1px 0;
  }

  .favourite-checkbox {
    float: right;
    cursor: pointer;
  }

  .favourite-checkbox > i {
    color: #dddddd;
    font-size: 32px;
    margin-bottom: 20px;
  }

  .favourite-checkbox.checked > i {
    color: #d06369;
  }

  #tags {
    display: flex;
    flex-wrap: wrap;
    flex-shrink: 0;
    gap: 8px;
  }

  .btn {
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
    text-align: center;
    cursor: pointer;
    border-radius: 1.5rem;
    transition: all 0.3s ease;
    border: 1px solid #3899a2;
    color: #363536;
  }

  @media (min-width: 1025px) {
    .btn:hover {
      border-color: #f78e09;
    }
    .tag:hover {
      background-color: #e08c8f;
    }
  }

  @media (max-width: 411px) {
    .btn {
      padding: 2px 4px;
      font-size: 6px;
    }
  }

  @media (min-width: 412px) and (max-width: 769px) {
    .btn {
      padding: 3px 6px;
      font-size: 8px;
    }
  }

  @media (min-width: 770px) and (max-width: 1024px) {
    .btn {
      padding: 4px 8px;
      font-size: 12px;
    }
    .btn:hover {
      border-color: unset;
    }
  }

  .tag {
    display: inline-block;
  }

  @media (max-width: 1024px) {
    .tag:hover {
      background-color: unset;
    }
    .tag:active {
      background-color: #e08c8f;
    }
  }

  .tag.checked {
    background-color: #36d183;
    border-color: #f78e09;
  }

  .reset-btn {
    float: right;
    background-color: #8bd2d5;
  }

  .reset-btn.disabled {
    background-color: #dddddd;
    border-color: #bbb;
  }

  .reset-btn:not(.disabled):hover {
    background-color: #3899a2;
    border-color: #f78e09;
  }
</style>
