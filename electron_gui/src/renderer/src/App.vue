<script setup>
import appBar from './components/appBar.vue'
import navigationDrawer from './components/navigationDrawer.vue'
import { useRouter } from 'vue-router'
import { useConfigStore } from '@renderer/stores/config'
const configStore = useConfigStore();
const router = useRouter();
router.push("/home")
function changeDrawer(drawer) {
  router.push(drawer)
}
</script>

<template>
  <v-app>
    <appBar></appBar>
    <v-main>
      <navigationDrawer @change-drawer="changeDrawer"></navigationDrawer>
      <RouterView />
    </v-main>
  </v-app>
</template>


<style>
</style>