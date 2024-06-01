<script setup>
import { ref } from 'vue'
import { useConfigStore } from '@renderer/stores/config'
const tab=ref('');
const shows= ref(false);
const configStore = useConfigStore();
configStore.getAllConfigs().then(()=>{
  configStore.initGuiConfig();
  tab.value=configStore.guiConfig.selectedConfig;
});

const barIcon= ref("mdi-chevron-down")
function setWin(state){
  if(state=="min"){
      window.setWin.min()
  }else if(state=="max"){
      window.setWin.max()
  }else if(state=="close"){
      window.setWin.close()
  }
}

function change(e){
  shows.value=!shows.value
  if(barIcon.value=="mdi-chevron-down"){
      barIcon.value="mdi-chevron-up"
  }else{
      barIcon.value="mdi-chevron-down"
  }
}
</script>

<template>
  <v-app-bar 
  :elevation="1"
  height="60"
  class="MainHeader"
  >
    <v-app-bar-title><v-img  src="../../public/BAAS.png" width="100"></v-img></v-app-bar-title>
    <v-app-bar-nav-icon class="noDrag" :icon="barIcon" @click="change"></v-app-bar-nav-icon>
    <v-app-bar-nav-icon class="noDrag" icon="mdi-window-minimize" @click="setWin('min')"></v-app-bar-nav-icon>
    <v-app-bar-nav-icon class="noDrag" icon="mdi-fullscreen"  @click="setWin('max')"></v-app-bar-nav-icon>
    <v-app-bar-nav-icon class="noDrag" icon="mdi-close"  @click="setWin('close')"></v-app-bar-nav-icon>
    <template v-slot:extension v-if="shows ">
        <v-tabs
        class="noDrag"
        v-model="tab"
        align-tabs="title"
        color="deep-purple-accent-4">
        <template v-for="item in Object.keys(configStore.userConfig)">
          <v-tab :value="item" color="blue" >{{item}}</v-tab>
        </template>
        
      </v-tabs>
      </template>
  </v-app-bar>
</template>

<style>
  
  .MainHeader {
      -webkit-app-region: drag;
  }
  .noDrag{
          -webkit-app-region: no-drag;
      }
</style>