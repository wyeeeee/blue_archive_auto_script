<script setup>
import featureSwitch from '@renderer/components/configurations/featureSwitch.vue'
import cafeInvite from '@renderer/components/configurations/cafeInvite.vue'
import schedulePriority from '@renderer/components/configurations/schedulePriority.vue'
import shopPriority from '@renderer/components/configurations/shopPriority.vue'
import arenaShopPriority from '@renderer/components/configurations/arenaShopPriority.vue'
import mainlinePriority from '@renderer/components/configurations/mainlinePriority.vue'
import arenaPriority from '@renderer/components/configurations/arenaPriority.vue'
import createPriority from '@renderer/components/configurations/createPriority.vue'
import totalForceFightPriority from '@renderer/components/configurations/totalForceFightPriority.vue'
import sweepCountConfig from '@renderer/components/configurations/sweepCountConfig.vue'
import {ref} from 'vue'
import { useConfigStore } from '@renderer/stores/config'
const configStore = useConfigStore();
configStore.getAllConfigs().then();
</script>

<template>
    <div class="text-h3 ma-5 mb-0" style="text-align: center;font-weight: 800; font-style: italic;"><span style="color: #128afa;">功能</span><span>开关</span> </div>
    <v-expansion-panels v-if="configStore.userConfig[configStore.guiConfig.selectedConfig]!=null" variant="inset" elevation="5" color="#128afa" class="pa-10"> 
        <v-expansion-panel v-for="switchConfig in configStore.userConfig[configStore.guiConfig.selectedConfig].switch" >
        
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
        <v-expansion-panel-text>
            <featureSwitch v-if="switchConfig.config=='featureSwitch'"></featureSwitch>
            <cafeInvite  v-else-if="switchConfig.config=='cafeInvite'"></cafeInvite>
            <schedulePriority  v-else-if="switchConfig.config=='schedulePriority'"></schedulePriority>
            <shopPriority  v-else-if="switchConfig.config=='shopPriority'"></shopPriority>
            <arenaShopPriority  v-else-if="switchConfig.config=='arenaShopPriority'"></arenaShopPriority>
            <mainlinePriority  v-else-if="switchConfig.config=='mainlinePriority'"></mainlinePriority>
            <arenaPriority  v-else-if="switchConfig.config=='arenaPriority'"></arenaPriority>
            <createPriority  v-else-if="switchConfig.config=='createPriority'"></createPriority>
            <totalForceFightPriority  v-else-if="switchConfig.config=='totalForceFightPriority'"></totalForceFightPriority>
            <sweepCountConfig  v-else-if="switchConfig.config=='sweepCountConfig'"></sweepCountConfig>
        </v-expansion-panel-text>
        </v-expansion-panel>
      </v-expansion-panels>
</template>