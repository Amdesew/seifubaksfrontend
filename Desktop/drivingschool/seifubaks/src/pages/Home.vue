<template>
  <meta name="csrf-token" content="{{ csrf_token }}">
  
  <div class="text-center py-40">
    <h1 class="text-3xl font-bold">Seifu Baks Driving School</h1>
  </div>

  <div class="mx-auto max-w-lg bg-gray-100 rounded-xl">
    <div class="grid grid-cols-2 py-5 border-b-8 border-white">
      <img src="@/assets/register.png" class="h-40 px-5" />
      <div>
        <p class="text-xl font-semibold py-8">
          Registration
        </p>
        <div class="px-1">
          <a class="bg-red-700 text-white px-7 py-3 rounded-full" href="/#register">Register</a>
        </div>
      </div>
    </div>

    <div class="grid grid-cols-2 py-5 border-b-8 border-white">
      <img src="@/assets/result.png" class="h-40 px-5" />
      <div>
        <p class="text-xl font-semibold py-8">
          Student Result
        </p>
        <div class="px-3">
          <a class="bg-red-700 text-white px-7 py-3 rounded-full" href="/Results">Show</a>
        </div>
      </div>
    </div>

    <div class="grid grid-cols-2 py-5">
      <img src="@/assets/tutors.png" class="h-40 px-5" />
      <div>
        <p class="text-xl font-semibold py-8">
          Class Tutorials
        </p>
        <div>
          <a class="bg-red-700 text-white px-7 py-3 rounded-full" href="/Tutorials">Get Started</a>
        </div>
      </div>
    </div>
  </div>

  <div class="text-center py-16" id="register">
    <h1 class="text-3xl font-bold">Register Here</h1>
    <form @submit.prevent="submitForm">
      <div class="py-10">
        <p class="text-xl">Full Name</p>
        <input class="border-b-2 border-black h-10 w-64" v-model="full_name"/>
        <p class="text-xl py-10">Phone Number</p>
        <input class="border-b-2 border-black h-10 w-64" v-model="phone_number"/>
        <p class="text-xl py-10">Wanted License</p>
        <input class="border-b-2 border-black h-10 w-64" v-model="wanted_licence"/>
        <div class="py-7">
          <button class="bg-red-700 py-3 px-10 text-white rounded-full" type="submit">Submit</button>
        </div>
      </div>
    </form>
  </div>

  <div class="text-center">
    <h1 class="text-2xl font-bold">Why Choose Us?</h1>
    <div class="py-6">
      <div class="bg-gray-100 mx-auto max-w-lg rounded-2xl border-b-8 border-white">
        <div class="grid grid-cols-2 px-20 py-10">
          <img src="@/assets/one.png" class="w-20"/>
          <p>Awarded Driving School In Amhara Region</p>
        </div>
      </div>

      <div class="bg-gray-100 mx-auto max-w-lg rounded-2xl border-b-8 border-white">
        <div class="grid grid-cols-2 px-20 py-10">
          <img src="@/assets/two.png" class="w-20"/>
          <p>The Most Digitalized Driving School With Modern Simulators</p>
        </div>
      </div>

      <div class="bg-gray-100 mx-auto max-w-lg rounded-2xl">
        <div class="grid grid-cols-2 px-20 py-10">
          <img src="@/assets/three.png" class="w-20"/>
          <p>The Best Technicians and Resourceful</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
"use client"
//import axios from 'axios';


export default {
  name: 'AppHome',

  data() {
    return {
      full_name: '',
      phone_number: '',
      wanted_licence: '',
    };
  },

  methods: {
    async submitForm() {
      // Retrieve CSRF token from meta tag
      const csrftokenElement = document.querySelector('meta[name="csrf-token"]');
      if (!csrftokenElement) {
        console.error('CSRF token not found in meta tag.');
        return;
      }
      const csrftoken = csrftokenElement.getAttribute('content');

      const formData = {
        full_name: this.full_name,
        phone_number: this.phone_number,
        wanted_licence: this.wanted_licence,
      };

      try {
        const response = await fetch('http://127.0.0.1:8000/api/NewStudent/', {
          method: 'POST',
          headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(formData),
          credentials: 'include', // Include cookies for CSRF
        });

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(`Error ${response.status}: ${errorData.detail || 'Unknown error'}`);
        }

        const data = await response.json();
        console.log('Form submitted successfully:', data);
        // Optionally, reset form fields
        this.full_name = '';
        this.phone_number = '';
        this.wanted_licence = '';
      } catch (error) {
        console.error('There was an error submitting the form:', error);
      }
    },
  },
};
</script>

<style scoped>
/* Add any necessary styles here */
</style>
