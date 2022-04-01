import { createApp, VueElement } from 'vue'
import App from './App.vue'
import axios from 'axios'
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import router from './routes/routes'
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css'

VueElement.prototype.$http=axios;


createApp(App).use(router, VueSweetalert2).mount('#app')
