import { createRouter, createWebHistory } from 'vue-router'

import loginPage from '../components/loginPage.vue'
import rulePage from '../components/rulePage.vue'
import socDashboard from '../components/socDashboard.vue'
import onBoard from '../components/onBoard.vue'
import result from '../components/result.vue'
import tablePage from '../components/tables.vue'
// import homeView from '@/views/HomeView.vue'
import homeView from '@/views/HomeView.vue'



const routes = [
  {
    name: 'login',
    path: '/',
    component: loginPage
  },
  {
    name: 'table',
    path: '/table',
    component: tablePage
  },
  {
    name: 'socdashboard',
    path: '/socdashboard',
    component: socDashboard
  },
  {
    name: 'home',
    path: '/home',
    component: homeView
  },
  {
    name: 'rules',
    path: '/rules',
    component: rulePage
  },
  {
    name: 'onBoard',
    path: '/onBoard',
    component: onBoard
  },
  {
    name: 'result',
    path: '/result',
    component: result
  },

]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  linkExactActiveClass: 'bg-purple-400'
})



// Create the router guard
router.beforeEach((to, from, next) => {
  const allowedPaths = ['/', ];

  if (allowedPaths.includes(to.path)) {

    next();
  } else {

    const user_id = sessionStorage.getItem('user_id')
    const username = sessionStorage.getItem('username')

    if ( user_id || username) {
      next();
    } else {
      next('/');
    }
  }
});


export default router
