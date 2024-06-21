<script setup>
    import { ref, watch } from 'vue'
    import { useConfigStore } from '@renderer/stores/config'
    const configStore = useConfigStore();
    configStore.getAllConfigs().then();
    var arenaShopList=ref([])
    if(configStore.guiConfig.server=='官服'){
        arenaShopList.value=configStore.staticConfig.tactical_challenge_shop_price_list.CN;
    }else if(configStore.guiConfig.server=='国际服'){
        arenaShopList.value=configStore.staticConfig.tactical_challenge_shop_price_list.Global;
    }else if(configStore.guiConfig.server=='B服'){
        arenaShopList.value=configStore.staticConfig.tactical_challenge_shop_price_list.CN;
    }else if(configStore.guiConfig.server=='日服'){
        arenaShopList.value=configStore.staticConfig.tactical_challenge_shop_price_list.JP;
    }
        </script>
    
    
        
        <template>
            <v-text-field label="刷新次数" density='compact' variant="outlined"  width="100" class="pt-2"></v-text-field>
            <div>
                <v-sheet class="d-inline-flex align-center pa-1"  v-for="items in arenaShopList">
                  <v-checkbox-btn class="d-flex" color="primary"></v-checkbox-btn>
                  <div class="text-body-2">
                    {{items[0]}}<br>
                    {{items[1]}}  
                  </div>
                </v-sheet>
                </div>
        </template>