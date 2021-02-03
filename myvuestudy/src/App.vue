
<!-- 展示模板 -->
<template>
  <div id="app">
    <img src="./assets/logo.png">
    <h1>{{msg}}</h1>
    <firstcomponent></firstcomponent>
    <secondcomponent></secondcomponent>
   </div>
</template>

<script>
import firstcomponent from './components/firstcomponent.vue'
import secondcomponent from './components/secondcomponent.vue'
export default{
 data(){
   return { msg:'我的页面'}
 },
 components: { firstcomponent,secondcomponent }
}
</script>
<!-- 样式代码 -->
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
