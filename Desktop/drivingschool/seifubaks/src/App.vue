<template>
  <body class="scroll-smooth">
      <Navbar/>
      <router-view></router-view>
      <AppFooters/>
      
  </body>

</template>

<script>
import "@/assets/tailwind.css"
import Navbar from "@/components/navbar.vue";
import AppFooters from "@/components/AppFooters.vue";

export default{
  name: 'App',
  components: {
    Navbar,
    AppFooters,
    
  }
}

</script>

<style>

</style>
