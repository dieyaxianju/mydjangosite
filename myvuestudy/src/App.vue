
<!-- 展示模板 -->
<template>
  <div id="app">
    <img src="./assets/logo.png">
    <h1>{{msg}}</h1>
    <router-view></router-view>
   </div>
</template>

<script>

export default{
 data(){
   return { msg:'我的页面，这个是app.vue页面，这个是公共部分'}
 }
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
