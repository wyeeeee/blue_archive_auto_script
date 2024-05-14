<template>
    <v-app id="inspire">

  

      <v-app-bar 
      :elevation="1"
      height="60"
      class="MainHeader"
      >

        <v-app-bar-title><v-img  src="../../public/BAAS.png" width="100"></v-img></v-app-bar-title>


        <v-app-bar-nav-icon class="noDrag" :icon="barIcon" @click="change"></v-app-bar-nav-icon>
        <v-app-bar-nav-icon class="noDrag" icon="mdi-window-minimize" ></v-app-bar-nav-icon>
        <v-app-bar-nav-icon class="noDrag" icon="mdi-fullscreen"></v-app-bar-nav-icon>
        <v-app-bar-nav-icon class="noDrag" icon="mdi-close"></v-app-bar-nav-icon>

        <template v-slot:extension v-if="shows ">
            <v-tabs
            class="noDrag"
            v-model="tab"
            align-tabs="title"
            color="deep-purple-accent-4"
            
          >
            <v-tab :value="1" color="blue">配置1</v-tab>
          </v-tabs>
          </template>
      </v-app-bar>
      <v-main>
        <v-navigation-drawer
        expand-on-hover
        rail
        width="200"
        mobile="false"
        permanent="true"
      >

        <v-list density="compact" nav>
          <v-list-item prepend-icon="mdi-home" title="home" value="myfiles" color="blue" ></v-list-item>
          <v-list-item prepend-icon="mdi-file-cog" title="configurations" value="shared" color="blue"></v-list-item>
          <v-list-item prepend-icon="mdi-cog" title="settings" value="starred" color="blue"></v-list-item>
        </v-list>
        <template v-slot:append>
            <v-list density="compact" nav>
                <v-list-item prepend-icon="mdi-help-box-multiple-outline" title="help" value="myfiles" color="blue"></v-list-item>
                <v-list-item prepend-icon="mdi-information-outline" title="about" value="shared" color="blue"></v-list-item>
              </v-list>
          </template>
      </v-navigation-drawer>
      <v-expansion-panels v-if="false">
        <v-expansion-panel>
        
        <v-expansion-panel-title>thik<br>sd</v-expansion-panel-title>
        <v-expansion-panel-text>sadwsadasdads</v-expansion-panel-text>
        </v-expansion-panel>
      </v-expansion-panels>
      </v-main>
    </v-app>
  </template>
  
  <script setup>
    import { ref } from 'vue'
  
    const shows= ref(false)
    const barIcon= ref("mdi-chevron-down")


    function change(e){
        shows.value=!shows.value
        if(barIcon.value=="mdi-chevron-down"){
            barIcon.value="mdi-chevron-up"
        }else{
            barIcon.value="mdi-chevron-down"
        }

        
    }
  </script>


  <style>
    
    .MainHeader {
        -webkit-app-region: drag;
    }
    .noDrag{
            -webkit-app-region: no-drag;
        }
  </style>