<template>
  <div id="firstcomponent">
    <h1>{{ msg }}</h1>
    <h2>Essential Links</h2>
    <a> written by {{ author }} </a>
  </div>
</template>

<script type="text/javascript">
export default {
  data() {
    return {
      author: '微信公众号 cc-love'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
