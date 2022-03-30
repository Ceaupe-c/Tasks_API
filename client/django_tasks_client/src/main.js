import { createApp, VueElement } from 'vue'
import App from './App.vue'
import axios from 'axios'
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css'

VueElement.prototype.$http=axios;

createApp(App).mount('#app')
