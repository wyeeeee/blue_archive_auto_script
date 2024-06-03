<script setup>
import { ref, watch } from 'vue'
import { useConfigStore } from '@renderer/stores/config'
const configStore = useConfigStore();
configStore.getAllConfigs().then();
var regionName=[]
if(configStore.guiConfig.server=='官服'){
  regionName=configStore.staticConfig.lesson_region_name.CN;
}else if(configStore.guiConfig.server=='国际服'){
  regionName=configStore.staticConfig.lesson_region_name.Global;
}else if(configStore.guiConfig.server=='B服'){
  regionName=configStore.staticConfig.lesson_region_name.CN;
}else if(configStore.guiConfig.server=='日服'){
  regionName=configStore.staticConfig.lesson_region_name.JP;
}
const schedule=ref({})
for (let i in regionName){
  schedule.value[regionName[i]]=[false,false,false,false,1];
}
</script>
    
    <template>
        <v-table>
            <thead>
              <tr>
                <th class="text-left">
                    区域名称
                  </th>
                <th class="text-left">
                  初级
                </th>
                <th class="text-left">
                    普通
                  </th>
                  <th class="text-left">
                    高级
                  </th>
                  <th class="text-left">
                    特级
                  </th>
                <th class="text-left">
                  日程次数
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(items,key) in schedule"
              >
              <td>{{key}}</td>
              <td>
                <v-checkbox-btn
                v-model="items[0]"
                color="primary"
                class="pe-2">
                </v-checkbox-btn>
            </td>
              <td>
                <v-checkbox-btn
                v-model="items[1]"
                color="primary"
                class="pe-2">
                </v-checkbox-btn>
            </td>
              <td>
                <v-checkbox-btn
                v-model="items[2]"
                color="primary"
                class="pe-2">
                </v-checkbox-btn>
            </td>
              <td>
                <v-checkbox-btn
                v-model="items[3]"
                color="primary"
                class="pe-2">
                </v-checkbox-btn>
            </td>
                <td>
                    <v-text-field label="次数" density='compact' variant="underlined" class="pt-3" v-model="items[4]"></v-text-field>
                </td>
              </tr>
            </tbody>
          </v-table>
    </template>