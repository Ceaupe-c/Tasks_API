<template>
  <div id="app">
    <TasksCrud />
  </div>
</template>

<script>

import TasksCrud from './components/TasksCrud.vue'

export default {
  name: 'App',
  components: {
    TasksCrud,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #5E5F76;
}
</style>
