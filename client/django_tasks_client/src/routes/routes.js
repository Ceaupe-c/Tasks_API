import { createRouter, createWebHashHistory,} from "vue-router"
import TaskCrud from '@/components/TasksCrud'
import AddTasks from '@/views/AddTasks'

const routes = [
    {
    path:'/',
    component: TaskCrud,
    name: 'taskcrud',
    }, 
    {
    path:'/AddTasks',
    component: AddTasks,
    name: 'addtasks'
    },
]

const router = createRouter({
    mode: 'history',
    history: createWebHashHistory(),
    routes
})

export default router