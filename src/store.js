import { collection, query } from "firebase/firestore";
import { ref, computed } from "vue";
import { useFirestore, useCollection } from "vuefire";

const db = useFirestore();
const companiesCol = collection(db, "companies");
export const companiesFilters = ref([null]);
const companiesQuery = computed(() => query(companiesCol, ...companiesFilters.value));
export const companies = useCollection(companiesQuery);
export const companiesTags = useCollection(collection(db, "tags"))
