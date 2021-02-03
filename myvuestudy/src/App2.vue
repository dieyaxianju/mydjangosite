
<!-- 展示模板 -->
<template>
<div id="app">
  <p>{{ message }}</p>
</div>
</template>

<script type="text/javascript">
export default{
 data(){
   return{ message:'我的页面'}
 },
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
