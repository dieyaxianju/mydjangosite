import Vue from 'vue'
import Router from 'vue-router'
//import Hello from '@/components/Hello'
//import about from '@/components/about'
import Login from '@/components/login/Login'

Vue.use(Router)

export default new Router({
  routes: [
//    {
//      path: '/',
//      name: 'Hello',
//      component: Hello
//    },
//    {
//      path: '/about',
//      name: 'about2',
//      component: about
//},
    {
      path: '/',
      name: 'Login',
      component: Login
}
  ]
})
