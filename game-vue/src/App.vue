<template>
  <div id="app">
    <!-- <Navbar :isLoggedIn="isLoggedIn"/>
     -->
     <Navbar/>
    <router-view />
  </div>
</template>

<script>

   import Navbar from './components/Navbar.vue';
    export default {
      data () {
        return {
          isLoggedIn: localStorage.getItem("token") !== null ? true : false
        }
      },
      components: {Navbar},
      methods: {
        logout () {
          alert('Logging out')
        }
      }
    }
</script>

<style>
</style>
