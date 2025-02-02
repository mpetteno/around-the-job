import '@/assets/main.css'
import '@/assets/leaflet.css'
import '@fortawesome/fontawesome-free/css/all.min.css';
import App from '@/App.vue'
import router from './router';
import { VueFire } from "vuefire";
import { createApp } from 'vue'
import { initializeApp } from 'firebase/app'
import { firebaseConfig } from "@/firebase-config.js";

const firebaseApp = initializeApp(firebaseConfig);
const app = createApp(App);
app.use(VueFire, {
  firebaseApp
})
app.use(router);
app.mount('#app');
