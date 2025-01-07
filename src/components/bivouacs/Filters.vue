<template>
  <Sidebar position="left">
    <label class="favourite-checkbox" :class="{checked: favouriteChecked}">
      <input type="checkbox" v-model="favouriteChecked" v-show="false"/>
      <i class="fa-heart" :class="favouriteChecked ? 'fa-solid': 'fa-regular'"></i>
    </label>
    <div id="filters">
      <label>
        <input type="checkbox" v-model="waterChecked" v-show="false"/>
        <i class="fa-solid fa-faucet-drip"></i>
        <span>Water</span>
      </label>
      <label>
        <input type="checkbox" v-model="woodChecked" v-show="false"/>
        <i class="fa-solid fa-tree"></i>
        <span>Wood</span>
      </label>
      <label>
        <input type="checkbox" v-model="kitchenChecked" v-show="false"/>
        <i class="fa-solid fa-kitchen-set"></i>
        <span>Kitchen</span>
      </label>
      <label>
        <input type="checkbox" v-model="fireplaceChecked" v-show="false"/>
        <i class="fa-solid fa-fire"></i>
        <span>Fireplace</span>
      </label>
      <label>
        <input type="checkbox" v-model="stoveChecked" v-show="false"/>
        <i class="fa-solid fa-fire-burner"></i>
        <span>Stove</span>
      </label>
    </div>
  </Sidebar>
</template>

<script setup>
import Sidebar from "@/ui/Sidebar.vue";
import { computed, ref, watch } from "vue";
import { collection, query, where } from "firebase/firestore";
import { useCollection, useFirestore } from "vuefire";
import { bivouacs } from '@/store.js'

// Get collections
const db = useFirestore();
const bivouacsCol = collection(db, "bivouacs");
const bivouacsFilters = ref([null]);
const bivouacsQuery = computed(() => query(bivouacsCol, ...bivouacsFilters.value));
useCollection(bivouacsQuery, { target: bivouacs })

// Favourite filter
const favouriteChecked = ref(false);
const favouriteFilter = computed(() => {
  return favouriteChecked.value ? [where("favourite", "==", favouriteChecked)] : []
});
// Water filter
const waterChecked = ref(false);
const waterFilter = computed(() =>
  waterChecked.value ? [where("water", "==", waterChecked)] : []
);
// Wood filter
const woodChecked = ref(false);
const woodFilter = computed(() =>
  woodChecked.value ? [where("wood", "==", woodChecked)] : []
);
// Kitchen filter
const kitchenChecked = ref(false);
const kitchenFilter = computed(() =>
  kitchenChecked.value ? [where("kitchen", "==", kitchenChecked)] : []
);
// Fireplace filter
const fireplaceChecked = ref(false);
const fireplaceFilter = computed(() =>
  fireplaceChecked.value ? [where("fireplace", "==", fireplaceChecked)] : []
);
// Stove filter
const stoveChecked = ref(false);
const stoveFilter = computed(() =>
  stoveChecked.value ? [where("stove", "==", stoveChecked)] : []
);

// Apply filters
const combinedFilters = computed(() => [
  ...favouriteFilter.value,
  ...waterFilter.value,
  ...woodFilter.value,
  ...kitchenFilter.value,
  ...fireplaceFilter.value,
  ...stoveFilter.value,
].flat());
bivouacsFilters.value = combinedFilters.value
watch([favouriteChecked, waterFilter, woodFilter, kitchenFilter, fireplaceFilter, stoveFilter], () => {
  bivouacsFilters.value = combinedFilters.value;
})
</script>

<style scoped>
.sidebar-container {
  height: 100%;
  max-width: 60%;
}

.sidebar-container >>> .sidebar {
  border-radius: 0 12px 12px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.sidebar-container >>> .toggle-button {
  height: 56px;
  width: 24px;
  border-radius: 0 24px 24px 0;
  border-width: 1px 1px 1px 0;
}

.favourite-checkbox {
  cursor: pointer;
}

.favourite-checkbox > i {
  color: #dddddd;
  font-size: 32px;
}

.favourite-checkbox.checked > i {
  color: #d06369;
}

#filters label {
  display: flex;
  align-items: center;
  padding: 12px 16px;
  margin: 10px 0;
  border: 1px solid #ddd;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
  background-color: #fff;
  font-size: 16px;
}

#filters label i {
  margin-right: 12px;
  font-size: 1.3em;
  color: #dddddd;
  transition: color 0.3s ease;
}

#filters label span {
  font-size: 0.95em;
  color: #444;
}


#filters label input:checked + i {
  color: #36d183;
}

@media (max-width: 768px) {
  .sidebar-container >>> .sidebar {
    height: auto !important;
  }
}

@media (min-width: 1025px) {
  #filters label:hover {
    background-color: #e08c8f;
  }
}

@media (max-width: 1024px) {
  #filters label:hover {
    background-color: unset;
  }
  #filters label:active {
    background-color: #e08c8f;
  }
}

</style>
