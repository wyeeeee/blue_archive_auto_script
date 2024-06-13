<script setup>
import { ref, watch } from 'vue'
import { useConfigStore } from '@renderer/stores/config'
const configStore = useConfigStore();
configStore.getAllConfigs().then();
const name=[];
for (let i in configStore.staticConfig.student_names){
  if(configStore.guiConfig.server=='官服' & configStore.staticConfig.student_names[i].CN_implementation==true){
    name.push({title:configStore.staticConfig.student_names[i].CN_name});
  }else if(configStore.guiConfig.server=='国际服' & configStore.staticConfig.student_names[i].Global_implementation==true){
    name.push({title:configStore.staticConfig.student_names[i].Global_name});
  }else if(configStore.guiConfig.server=='B服' & configStore.staticConfig.student_names[i].CN_implementation==true){
    name.push({title:configStore.staticConfig.student_names[i].CN_name});
  }else if(configStore.guiConfig.server=='日服' & configStore.staticConfig.student_names[i].JP_implementation==true){
    name.push({title:configStore.staticConfig.student_names[i].JP_name});
  }
}

const cafeInvite = ref({
cafe_reward_collect_hour_reward:{
        enable:false,
        value:'是否要领取奖励',
        type:'checkbox'
    },
    cafe_reward_use_invitation_ticket:{
        enable:false,
        value:'是否使用邀请券',
        type:'checkbox'
    },
    cafe_reward_lowest_affection_first:{
        enable:false,
        value:'优先邀请好感等级低的学生',
        type:'checkbox'
    },
    cafe_reward_choose_students:{
        selects:[],
        show:true,
        value:'选择你要添加邀请的学生',
        type:'selects',
        items:name
    },
    cafe_reward_choose_way_of_touching:{
        selects:[],
        show:true,
        value:'选择摸头方式',
        type:'selects',
        title:'CN_name',
        items:[configStore.userConfig[configStore.guiConfig.selectedConfig].config.patStyle]
    },
    cafe_reward_have_second_cafe:{
        enable:false,
        value:'是否有二号咖啡厅',
        type:'checkbox'
    },
    cafe_reward_choose_students2:{
        selects:[],
        show:false,
        value:'选择你要添加邀请的学生',
        type:'selects',
        title:'CN_name',
        items:name
    }
})

watch(()=>cafeInvite.value.cafe_reward_have_second_cafe.enable,(newValue)=>{
    if(newValue==true){
        cafeInvite.value.cafe_reward_choose_students2.show=true
    }else{
        cafeInvite.value.cafe_reward_choose_students2.show=false
    }
  })
</script>
    
    <template>
        <template v-for="components in cafeInvite">
        <v-card variant="text" v-if="components.type == 'checkbox'">
            <v-card-text>
              <v-sheet class="d-inline-flex  align-center">
                <v-switch
                v-model="components.enable"
                color="primary"
                class="d-flex"
              ></v-switch>
                <div class="text-body-1">
                  {{ components.value}}
                </div>
              </v-sheet>
            </v-card-text>
          </v-card>
          <v-select class="pt-2 pa-1" multiple variant="solo" v-if="components.type == 'selects' & components.show==true" :items="components.items" item-title="title" :label="components.value">
        </v-select>
        <v-divider></v-divider>
        </template>


    </template>