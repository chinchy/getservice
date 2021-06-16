import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home';
import SignIn from '@/views/auth/SignIn';
import SignUp from '@/views/auth/SignUp';
import Office from '@/views/data/Office';
import Entries from '@/views/data/Entries';
import Employees from "@/views/data/Employees";
import Services from "@/views/data/Services";
import Positions from "@/views/data/Positions";
import Prices from "@/views/data/Prices";
import Clients from "@/views/data/Clients";
import Reports from "@/views/data/Reports";

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [{
      path: '/',
      name: 'Home',
      component: Home,
    },{
      path: '/auth/signin',
      name: 'SignIn',
      component: SignIn,
    },
    {
      path: '/auth/signup',
      name: 'SignUp',
      component: SignUp,
    },
    {
      path: '/offices',
      name: 'Offices',
      component: Office,
    },
    {
      path: '/entries',
      name: 'Entries',
      component: Entries,
    },
    {
      path: '/employees',
      name: 'Employees',
      component: Employees,
    },
    {
      path: '/services',
      name: 'Services',
      component: Services,
    },
    {
      path: '/positions',
      name: 'Positions',
      component: Positions,
    },
    {
      path: '/prices',
      name: 'Prices',
      component: Prices,
    },
    {
      path: '/clients',
      name: 'Clients',
      component: Clients,
    },
    {
      path: '/reports',
      name: 'Reports',
      component: Reports,
    }
  ],
});

// const routes = [
//   {
//     path: '/',
//     name: 'Home',
//     component: Home
//   },
//   {
//     path: '/about',
//     name: 'About',
//     // route level code-splitting
//     // this generates a separate chunk (about.[hash].js) for this route
//     // which is lazy-loaded when the route is visited.
//     component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
//   }
// ]
//
// const router = new Router({
//   routes
// })
//
// export default router
