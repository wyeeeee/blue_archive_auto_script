<script setup>
    import { ref } from 'vue'
    const includeFiles = ref([])
const props = defineProps({
    switchConfig: Object
})
    </script>
    
    <template>
        <v-card variant="text">
            <v-card-text>
              <div class="d-flex pa-1">
                <v-checkbox-btn
                  v-model="includeFiles"
                  class="pe-2"
                ></v-checkbox-btn>
                <v-text-field
                  label="Include files"
                  hide-details
                ></v-text-field>
              </div>
            </v-card-text>
          </v-card>
          <v-card variant="text">
            <v-card-text>
              <div class="d-flex pa-1">
                <v-checkbox-btn
                  v-model="includeFiles"
                  class="pe-2"
                ></v-checkbox-btn>
                <v-text-field
                  label="Include files"
                  hide-details
                ></v-text-field>
              </div>
            </v-card-text>
          </v-card>
    </template>