<template>
    <div class="text-center">
        <h1 class="text-3xl py-20 font-bold">Practical Exam Result</h1>

        <div>
            <h2 class="text-xl">Check Out Your Result</h2>
            
            <div class="py-7">
                <input v-model="studentId" class="border-black border-b-2" placeholder="Enter Your Id"/>
                
                <div class="py-5">
                    <button class="py-3 px-7 rounded-full text-white bg-red-800" @click="fetchResult">Check</button>
                </div>
            </div>
        </div>
    </div>

    <div v-if="result">
        <h2 class="text-xl font-bold">Your Result:</h2>
        <p class="text-center text-xl">{{ result }}</p>
    </div>

    <div v-if="error" class="text-red-600 text-xl text-center">
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


export default{
    name: 'PageResult',
    data(){
        return {
            studentId: '',
            result: null,
            error: null,
        }
    },
    methods: {
        async fetchResult() {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/NewStudent/`, {
                    params: { id: this.studentId }
                });
                this.result = response.data.result;
                this.error = null;
            } catch (error) {
                this.error = error.response ? error.response.data.error : 'Network Error';
                this.result = null;
            }
        }
    }
}

</script>