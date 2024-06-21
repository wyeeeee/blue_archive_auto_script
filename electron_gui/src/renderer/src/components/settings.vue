<script setup>
import emulatorConfig from "@renderer/components/settings/emulatorConfig.vue"
import eventMapConfig from "@renderer/components/settings/eventMapConfig.vue"
import exploreConfig from "@renderer/components/settings/exploreConfig.vue"
import hardTaskConfig from "@renderer/components/settings/hardTaskConfig.vue"
import otherConfig from "@renderer/components/settings/otherConfig.vue"
import proceedPlot from "@renderer/components/settings/proceedPlot.vue"
import pushConfig from "@renderer/components/settings/pushConfig.vue"
import scriptConfig from "@renderer/components/settings/scriptConfig.vue"
import serverConfig from "@renderer/components/settings/serverConfig.vue"


import { ref } from 'vue';
const baseConfigs = ref([
  {
    name: '应用相关设置',
    tip: '选择你的服务器平台，设置你的端口（不知道端口请设置为0）',
    component:serverConfig
  },
  {
    name: '脚本相关设置',
    tip: '根据你的电脑配置，调整相应的参数。',
    component:scriptConfig
  },
  {
    name: "模拟器启动设置",
    tip:"设置启动模拟器的路径",
    component:emulatorConfig}])

const otherConfigs = ref([
  {
    name: '普通图推图设置',
    tip: '根据你所需困难图刷关，设置参数。',
    component:exploreConfig
  },
  {
    name: '困难图推图设置',
    tip: '根据你所需困难图刷关，设置参数。',
    component:hardTaskConfig
  },
  {
    name:'推剧情',
    tip:'推故事，推任务，推挑战',
    component:proceedPlot},  
    {
    name: '活动图设置',
    tip: '根据你所需困难图刷关，设置参数。',
    component:eventMapConfig
  },
  {
    name: '其他设置',
    tip: '其他的一些小功能与设置',
    component:otherConfig
  },
  {
    name:'推送设置',
    tip:'推送信息',
    component:pushConfig},])
</script>

<template>
    <div class="text-h3 ma-5 mb-0" style="text-align: center;font-weight: 800; font-style: italic;"><span style="color: #128afa;">基本</span><span>设置</span> </div>
    <v-expansion-panels v-if="baseConfigs!=null" variant="inset" elevation="5" color="#128afa" class="pa-10" > 
        <v-expansion-panel v-for="baseConfig in baseConfigs" >
        
        <v-expansion-panel-title>
            <v-card
            prepend-icon="mdi-book-cog"
            :subtitle="baseConfig.tip"
            variant="text"
            height="70"
            width="600"
          >
            <template v-slot:title>
              <span class="font-weight-black">{{baseConfig.name}}</span>
            </template>
          </v-card>
        </v-expansion-panel-title>
        <v-expansion-panel-text>
          <component :is="baseConfig.component"></component>
        </v-expansion-panel-text>
        </v-expansion-panel>
      </v-expansion-panels>
    <div class="text-h3 ma-5 mb-0" style="text-align: center;font-weight: 800; font-style: italic;"><span style="color: #128afa;">相关</span><span>设置</span> </div>
    <v-expansion-panels v-if="otherConfigs!=null" variant="inset" elevation="5" color="#128afa" class="pa-10" > 
        <v-expansion-panel v-for="otherConfig in otherConfigs" >
        
        <v-expansion-panel-title>
            <v-card
            prepend-icon="mdi-book-cog"
            :subtitle="otherConfig.tip"
            variant="text"
            height="70"
            width="600"
          >
            <template v-slot:title>
              <span class="font-weight-black">{{otherConfig.name}}</span>
            </template>
          </v-card>
        </v-expansion-panel-title>
        <v-expansion-panel-text>
          <component :is="otherConfig.component"></component>
        </v-expansion-panel-text>
        </v-expansion-panel>
      </v-expansion-panels>
</template>