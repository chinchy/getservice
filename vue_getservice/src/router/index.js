import Vue from 'vue'
import Router from 'vue-router'
import SignIn from '@/views/auth/SignIn';
import SignUp from '@/views/auth/SignUp';
import Office from '@/views/data/Office';

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [{
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
