// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueRouter from 'vue-router'
import store from './store'

// 引入element-ui的js文件
import ElementUI from 'element-ui'
// 引入element-ui的css文件
import 'element-ui/lib/theme-chalk/index.css'

// 导入axios
import axios from 'axios'
import QS from 'qs'

// 引入quill
import VueQuillEditor from 'vue-quill-editor'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'

Vue.use(VueQuillEditor)

// 导入echarts
// import echarts from 'echarts'
// Vue.prototype.$echarts = echarts

Vue.prototype.$axios = axios
Vue.prototype.qs = QS

Vue.config.productionTip = false

Vue.use(VueRouter)
Vue.use(ElementUI)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store: store,
  // components: { App },
  // template: '<App/>'
  render: h => h(App)
})
