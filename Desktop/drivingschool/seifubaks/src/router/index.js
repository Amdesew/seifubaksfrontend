import {createRouter, createWebHistory} from 'vue-router';
import PageResult from "@/pages/Result.vue";
import AppHome from "@/pages/Home.vue";
import AppTutorials from "@/pages/Tutorials.vue"



const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes: [{
        path: '/Results',
        name: 'Results',
        component: PageResult
    },
    {
        path: '/Home',
        name: 'Home_one',
        component: AppHome
    },
    {
        path: '',
        name: 'Home',
        component: AppHome
    },
    {
        path: '/Tutorials',
        name: 'Tutorials',
        component: AppTutorials
    }
]
})

export default router;