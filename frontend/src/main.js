// src/main.js
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import './assets/styles.css'; // Import the global CSS file

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');