<script setup>
import { ref } from 'vue';
const baseConfigs = ref([
  {
    name: '应用相关设置',
    tip: '选择你的服务器平台，设置你的端口（不知道端口请设置为0）',
  },
  {
    name: '脚本相关设置',
    tip: '根据你的电脑配置，调整相应的参数。',
  },
  {
    name: "模拟器启动设置",
    tip:"设置启动模拟器的路径"}])

const otherConfigs = ref([
  {
    name: '普通图推图设置',
    tip: '根据你所需困难图刷关，设置参数。',
  },
  {
    name: '困难图推图设置',
    tip: '根据你所需困难图刷关，设置参数。',
  },
  {
    name:'推剧情',
    tip:'推故事，推任务，推挑战'},  
    {
    name: '活动图设置',
    tip: '根据你所需困难图刷关，设置参数。',
  },
  {
    name: '其他设置',
    tip: '其他的一些小功能与设置',
  },
  {
    name:'推送设置',
    tip:'推送信息'},])
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
        <v-expansion-panel-text v-for="i in 10">{{baseConfig.name}}</v-expansion-panel-text>
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
        <v-expansion-panel-text v-for="i in 10">{{otherConfig.name}}</v-expansion-panel-text>
        </v-expansion-panel>
      </v-expansion-panels>
</template>