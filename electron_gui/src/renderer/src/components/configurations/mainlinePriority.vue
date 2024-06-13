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
                  label="普通关卡与次数"
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
                  label="困难关卡设置同上"
                  hide-details
                  variant="underlined"
                ></v-text-field>
              </div>
            </v-card-text>
          </v-card>
    </template>