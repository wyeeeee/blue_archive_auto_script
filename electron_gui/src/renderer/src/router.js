import { createMemoryHistory, createRouter } from 'vue-router'
import home from './components/home.vue'
import help from './components/help.vue'
import about from './components/about.vue'
import settings from './components/settings.vue'
import configurations from './components/configurations.vue'

const routes = [
  { path: '/home', component: home },
  { path: '/settings', component: settings },
  { path: '/configurations', component: configurations },
  { path: '/help', component: help },
  { path: '/about', component: about },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router