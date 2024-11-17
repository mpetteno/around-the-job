import '@/assets/main.css'
import { VueFire } from "vuefire";
import { getFirebase } from './firebase'
import { createApp } from 'vue'
import App from './App.vue'

const { firebaseConfig } = getFirebase();
const app = createApp(App)
  .use(VueFire, {
    firebaseApp: firebaseConfig
  })

app.mount('#app');
