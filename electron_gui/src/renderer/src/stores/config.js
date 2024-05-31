import { defineStore } from 'pinia'
import {ref} from 'vue'
const userConfigType=[
  'config',
  'display',
  'event',
  'switch',
]
export const useConfigStore = defineStore('config', ()=>{
      const staticConfig=ref({});
      const userConfig=ref({});

      function getAllConfigs(){
        window.api.config.getConfig('static').then(config=>{
          staticConfig.value=JSON.parse(config) ;
        })
        window.api.config.getConfigName()
        .then(name=>{
            for(let i in name){
              if (Object.keys(userConfig.value).length === 0){userConfig.value[name[i]]={};}
              for (let j in userConfigType){
                window.api.config.getConfig(userConfigType[j],name[i])
                .then(config=>{
                  userConfig.value[name[i]][userConfigType[j]]=JSON.parse(config);
                })
              }
            }
        }
        )
      }
    
      return{staticConfig,userConfig,getAllConfigs}
})