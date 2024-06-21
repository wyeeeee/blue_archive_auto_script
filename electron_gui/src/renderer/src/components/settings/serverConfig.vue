<script setup>
    import { ref, watch } from 'vue'
    import { useConfigStore } from '@renderer/stores/config'
    const configStore = useConfigStore();
    configStore.getAllConfigs().then();
    var server=ref(['官服', 'B服', '国际服', '日服'])

        </script>
    
    
        
        <template>
            <v-select class="pt-2 pa-1" multiple variant="solo" :items="server" label="server"></v-select>
            <v-card variant="text">
                <v-card-text>
                  <div class="d-flex pa-1">
                    <v-text-field
                      label="adb端口号"
                      hide-details
                      variant="underlined"
                    ></v-text-field>
                  </div>
                </v-card-text>
              </v-card>
        </template>