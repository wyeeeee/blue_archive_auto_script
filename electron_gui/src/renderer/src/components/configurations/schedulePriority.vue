<script setup>
import { ref, watch } from 'vue'
import { useConfigStore } from '@renderer/stores/config'
const configStore = useConfigStore();
configStore.getAllConfigs().then();
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
              <tr v-for="i in 10"
              >
              <td>www</td>
              <td>
                <v-checkbox-btn
                color="primary"
                class="pe-2">
                </v-checkbox-btn>
            </td>
              <td>
                <v-checkbox-btn
                color="primary"
                class="pe-2">
                </v-checkbox-btn>
            </td>
              <td>
                <v-checkbox-btn
                color="primary"
                class="pe-2">
                </v-checkbox-btn>
            </td>
              <td>
                <v-checkbox-btn
                color="primary"
                class="pe-2">
                </v-checkbox-btn>
            </td>
                <td>
                    <v-text-field label="次数" density='compact' variant="underlined" class="pt-3"></v-text-field>
                </td>
              </tr>
            </tbody>
          </v-table>
    </template>