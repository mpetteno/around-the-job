import '@/assets/main.css'
import { VueFire } from "vuefire";
import { createApp } from 'vue'
import App from '@/App.vue'
import { initializeApp } from 'firebase/app'
import { firebaseConfig } from "@/firebase-config.js";

const firebaseApp = initializeApp(firebaseConfig);
const app = createApp(App);
app.use(VueFire, {
  firebaseApp
})
app.mount('#app');
