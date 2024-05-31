import './assets/main.css'
import '@mdi/font/css/materialdesignicons.css'
import { createApp } from 'vue'
import { aliases, mdi } from 'vuetify/iconsets/mdi'
// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import router from './router'
// Components
import App from './App.vue'
//pinia
import { createPinia } from 'pinia'
const pinia = createPinia()
const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi,
    },
  },
})
const app = createApp(App)
app.use(router)
app.use(vuetify)
app.use(pinia)
app.mount('#app')