<script setup>
import { ref, watch } from 'vue'
import { useConfigStore } from '@renderer/stores/config'
const configStore = useConfigStore();
configStore.getAllConfigs().then();
var shopList=ref([])
if(configStore.guiConfig.server=='官服'){
  shopList.value=configStore.staticConfig.common_shop_price_list.CN;
}else if(configStore.guiConfig.server=='国际服'){
  shopList.value=configStore.staticConfig.common_shop_price_list.Global;
}else if(configStore.guiConfig.server=='B服'){
  shopList.value=configStore.staticConfig.common_shop_price_list.CN;
}else if(configStore.guiConfig.server=='日服'){
  shopList.value=configStore.staticConfig.common_shop_price_list.JP;
}
</script>
    
<template>
    <template v-for="items in shopList">
    <v-checkbox class="float-left" color="primary">
        <template v-slot:label>
          <div>{{items[0]}}
          </div>
        </template>
      </v-checkbox>
    </template>
</template>