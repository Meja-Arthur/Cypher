import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import axios from 'axios'

axios.defaults.baseURL = ' http://127.0.0.1:8000/'
// base url which is the default http from the frontend
// this prevent's the use full url in the axios part while fetching information from the backend part

createApp(App).use(store).use(router, axios).mount('#app')
