<template>

    <div class="text-center">
        <h1 class="text-3xl py-20 font-bold">Practical Exam Result</h1>

        <div>
            <h2 class="text-xl">Check Out Your Result</h2>
            
            <div class="py-7">
                <input v-model="searchId" class="border-black border-b-2" placeholder="Enter Your Id"/>
                
                <div class="py-5">
                    <button class="py-3 px-7 rounded-full text-white bg-red-800" @click="fetchStudentResult">Check</button>
                </div>
            </div>
        </div>
    </div>

    <div v-if="studentResult">
        <p class="text-xl font-bold text-center">Full Name: {{ studentResult.full_name }}</p>
        <p class="text-center text-xl">Result: {{ studentResult.result }}</p>
    </div>

    <div v-else-if="loading" class="text-red-600 text-xl text-center">
        <p>Loading</p>
    </div>
    <div v-else-if="error">
      <p>{{ error }}</p>
    </div>

    <div class="text-center py-36">
        <h2 class="text-2xl font-semibold">Grading System</h2>

        <div class="py-10">
            <div class="grid grid-cols-2 mx-auto max-w-lg px-20 ">
                <img src="@/assets/passed_icon.png" class="w-28">
                <p>In Order To Pass The Practical Exam You Need To Get Over 74%</p>
            </div>

            <div class="grid grid-cols-2 mx-auto max-w-lg px-20 py-14 ">
                <img src="@/assets/failed_icon.jpg" class="w-28">
                <p>If Your Grade Is Below 74% You Will Fail</p>
            </div>
        </div>

        <div>
            <h1 class="text-center text-2xl font-semibold">What Happens If I Fail ?</h1>

            <div class="grid grid-cols-2 mx-auto max-w-lg px-20 py-14 ">
                <img src="@/assets/examiner.png" class="w-28">
                <p>You Will Get A Chance To Take The Test Again 2 Times</p>
            </div>

        </div>

    </div>

    


</template>

<script>
import axios from 'axios';

export default {
    name: 'PageResult',
    data() {
        return {
        searchId: '',
        studentResult: null,
        loading: false,
        error: null,
        };
    },
    methods: {
        fetchStudentResult() {
        if (!this.searchId) {
            this.error = 'Please enter a student ID.';
            return;
        }
        this.loading = true;
        this.error = null;
        axios.get(`http://127.0.0.1:8000/api/StudentResult/${this.searchId}`)
            .then(response => {
            console.log('Result: ', response.data)
            this.studentResult = response.data;
            this.loading = false;
            })
            .catch( error => {
            console.log(error)
            this.error = 'There was an error fetching the student result.';
            this.loading = false;
            });
        },
    },
    };
</script>