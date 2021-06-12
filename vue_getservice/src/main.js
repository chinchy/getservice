import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import axios from "axios"
import VueAxios from "vue-axios"
import Vuelidate from 'vuelidate'

Vue.config.productionTip = false
Vue.use(VueAxios, axios)
Vue.use(Vuelidate)

new Vue({
  router,
  render: h => h(App),
  axios
}).$mount('#app')
