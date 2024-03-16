import './assets/style.css'
import 'flowbite';
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
// require('dotenv').config()

const app = createApp(App)


app.use(createPinia())
app.use(router)

app.mount('#app')
