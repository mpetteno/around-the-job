import { createRouter, createWebHistory } from 'vue-router';
import CompaniesMap from '../components/companies/Map.vue';
import BivouacsMap from '../components/bivouacs/Map.vue';

const routes = [
  { path: '/companies', component: CompaniesMap },
  { path: '/bivouacs', component: BivouacsMap },
  { path: '/:pathMatch(.*)*', redirect: '/companies' }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
