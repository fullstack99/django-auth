import Vue from "vue";
import VueRouter from "vue-router";
import Login from "../views/Login.vue";
import Register from "../views/Signup.vue";
import Dashboard from "../views/Dashboard.vue";
import store from '../store';
Vue.use(VueRouter);

const routes = [
  {
    path: "/login",
    name: "Login",
    component: Login
  },
  {
    path: "/register",
    name: "Register",
    component: Register
  },
  {
    path: "/",
    name: "Dashboard",
    component: Dashboard
  },
  { path: '*', redirect: '/' }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = store.state.auth.authenticated;

  if(to.path == '/login'|| to.path == '/register') {
    if (isAuthenticated) {
      next('/');
    } else {
      next();
    }
  } else {
    if (isAuthenticated) {
      next();
    } else {
      next('/login');
    }
  }

});

export default router;
