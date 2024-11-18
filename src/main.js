import '@/assets/main.css'
import { VueFire } from "vuefire";
import { getFirebase } from './firebase'
import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)
  .use(VueFire, {
    firebaseApp: getFirebase()
  })

app.mount('#app');
