<script setup>
import {ref} from 'vue';
const switchConfigs = ref(null);
switchConfigs.value=JSON.parse(await window.api.config.getConfig('default_config',"switch"))
</script>

<template>
    <div class="text-h3 ma-5 mb-0" style="text-align: center;font-weight: 800; font-style: italic;"><span style="color: #128afa;">功能</span><span>开关</span> </div>
    <v-expansion-panels v-if="switchConfigs!=null" variant="inset" elevation="5" color="#128afa" class="pa-10"> 
        <v-expansion-panel v-for="switchConfig in switchConfigs" >
        
        <v-expansion-panel-title>
            <v-card
            prepend-icon="mdi-book"
            :subtitle="switchConfig.tip"
            variant="text"
            height="70"
            width="600"
          >
            <template v-slot:title>
              <span class="font-weight-black">{{switchConfig.name}}</span>
            </template>
          </v-card>
        </v-expansion-panel-title>
        <v-expansion-panel-text v-for="i in 10">{{switchConfig.name}}</v-expansion-panel-text>
        </v-expansion-panel>
      </v-expansion-panels>
</template>