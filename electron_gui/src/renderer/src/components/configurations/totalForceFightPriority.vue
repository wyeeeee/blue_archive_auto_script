<script setup>
import { ref, watch } from 'vue'
import { useConfigStore } from '@renderer/stores/config'
const configStore = useConfigStore();
configStore.getAllConfigs().then();
var challenging=ref([])
if(configStore.guiConfig.server=='官服'){
    challenging.value=configStore.staticConfig.total_assault_difficulties.CN;
}else if(configStore.guiConfig.server=='国际服'){
    challenging.value=configStore.staticConfig.total_assault_difficulties.Global;
}else if(configStore.guiConfig.server=='B服'){
    challenging.value=configStore.staticConfig.total_assault_difficulties.CN;
}else if(configStore.guiConfig.server=='日服'){
    challenging.value=configStore.staticConfig.total_assault_difficulties.JP;
}
    </script>
    
    <template>
        <v-select class="pt-2 pa-1" multiple variant="solo" :items="challenging" label="最高难度"></v-select>
    </template>