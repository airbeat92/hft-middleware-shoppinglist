import { createRouter, createWebHistory } from 'vue-router'
import ShoppinglistView from "@/views/ShoppinglistView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: ShoppinglistView
    }
  ]
})

export default router
