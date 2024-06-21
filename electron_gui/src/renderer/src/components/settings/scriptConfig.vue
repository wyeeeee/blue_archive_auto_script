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
                      label="截图间隔"
                      hide-details
                      variant="underlined"
                    ></v-text-field>
                  </div>
                </v-card-text>
              </v-card>
        </template>