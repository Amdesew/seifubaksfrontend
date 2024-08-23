<template>
    <nav class="bg-red-900 p-4">
        <div class="container mx-auto flex justify-between items-center">
        <!-- Logo -->
        <a href="/" class="text-white text-xl font-bold">Seifu Baks Driving School</a>
        
        <!-- Menu for larger screens -->
        <div class="hidden md:flex space-x-4">
            <a href="/Home" class="text-gray-300 hover:text-white">Home</a>
            <a href="/Home#register" class="text-gray-300 hover:text-white" >Register</a>
            <router-link to="/Results" class="text-gray-300 hover:text-white">Results</router-link>
            <a href="/Tutorials" class="text-gray-300 hover:text-white">Tutorials</a>
        </div>
        
        
        
        <!-- Mobile Menu Button -->
        <div class="md:hidden">
            <button id="menu-btn" class="text-gray-300 hover:text-white">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
            </button>
        </div>
        </div>

        <!-- Mobile Menu -->
        <div id="mobile-menu" class="hidden md:hidden">
        <a href="/Home" class="block text-gray-300 hover:text-white px-4 py-2">Home</a>
        <a href="/Home#register" class="block text-gray-300 hover:text-white px-4 py-2">Register</a>
        <a href="/Results" class="block text-gray-300 hover:text-white px-4 py-2">Results</a>
        <a href="/Tutorials" class="block text-gray-300 hover:text-white px-4 py-2">Tutorials</a>
        </div>
    </nav>
    
</template>

    
  

<script>
import '@/assets/tailwind.css'




export default{
    name: 'NavBar',
    mounted(){
        const menuBtn = document.getElementById('menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');

        menuBtn.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
        }); 
    }
}


</script>

<style>

</style>