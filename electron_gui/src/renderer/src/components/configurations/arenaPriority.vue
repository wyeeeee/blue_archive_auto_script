<script setup>
import { ref, watch } from 'vue'
import { useConfigStore } from '@renderer/stores/config'
const configStore = useConfigStore();
configStore.getAllConfigs().then();
    </script>
    
    <template>
        <v-card variant="text">
            <v-card-text>
              <div class="d-flex pa-1">
                <v-text-field
                  label="输入你需要对手比你低几级，高几级则填负数"
                  hide-details
                  variant="underlined"
                ></v-text-field>
              </div>
            </v-card-text>
          </v-card>
          <v-card variant="text">
            <v-card-text>
              <div class="d-flex pa-1">
                <v-text-field
                  label="输入你最多需要刷新几次"
                  hide-details
                  variant="underlined"
                ></v-text-field>
              </div>
            </v-card-text>
          </v-card>
    </template>