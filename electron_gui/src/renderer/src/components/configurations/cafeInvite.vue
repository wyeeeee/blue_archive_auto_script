<script setup>
import { ref } from 'vue'
import { useConfigStore } from '@renderer/stores/config'
const configStore = useConfigStore();
configStore.getAllConfigs().then();
const cafeInvite = ref({
cafe_reward_collect_hour_reward:{
        enable:false,
        value:'是否要领取奖励',
        type:'checkbox',
        fun:()=>{
            console.log('cafe_reward_collect_hour_reward')
        }
    },
    cafe_reward_use_invitation_ticket:{
        enable:false,
        value:'是否使用邀请券',
        type:'checkbox',
        fun:()=>{
            console.log('cafe_reward_collect_hour_reward')
        }
    },
    cafe_reward_lowest_affection_first:{
        enable:false,
        value:'优先邀请好感等级低的学生',
        type:'checkbox',
        fun:()=>{
            console.log('cafe_reward_collect_hour_reward')
        }
    },

})
</script>
    
    <template>
        <template v-for="items in cafeInvite">
        <v-card variant="text" v-if="items.type == 'checkbox'">
            <v-divider></v-divider>
            <v-card-text>
              <div class="d-flex pa-1">
                <v-checkbox-btn
                  v-model="items.enable"
                  color="primary"
                  class="pe-2"
                  @click="items.fun"
                ></v-checkbox-btn>
                <div class="text-h6">
                  {{ items.value}}
                </div>
              </div>
            </v-card-text>
          </v-card>

        </template>
        <v-divider></v-divider>
        <v-select class="pt-5 pa-1" multiple variant="solo" :items="configStore.staticConfig.student_names" item-title="CN_name" label="选择你要添加邀请的学生">
            <template v-slot:prepend-item>
                <v-list-item
                  title="全选"
                  @click="toggle"
                >
                  <template v-slot:prepend>
                    <v-checkbox-btn
                      :model-value="likesAllFruit"
                    ></v-checkbox-btn>
                  </template>
                </v-list-item>
          
                <v-divider class="mt-2"></v-divider>
              </template>
          
              <template v-slot:append-item>
          
                <v-list-item
                  :subtitle="subtitle"
                  :title="title"
                  disabled
                >
                </v-list-item>
              </template>
        </v-select>
    </template>