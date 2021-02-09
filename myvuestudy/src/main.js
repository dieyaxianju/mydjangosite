// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App' /*引入App这个组件*/
import router from './router'/*引入路由配置*/
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

//自己写的样式
import './style/theme.css'
import './style/character.css'

// 注册element-ui
Vue.use(ElementUI)

Vue.config.productionTip = false


//开启debug模式
Vue.config.debug = true;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {App},/*告知当前页面想使用App这个组件*/
  template: '<App/>' /*告知页面这个组件用这样的标签来包裹着,并且使用它*/
})
