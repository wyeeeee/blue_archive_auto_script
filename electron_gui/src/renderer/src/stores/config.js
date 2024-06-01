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
      const guiConfig=ref({
        selectedConfig:null,
        server:null,
      });
      async function getAllConfigs(){
        staticConfig.value=JSON.parse(await window.api.config.getConfig('static')) ;
        let name=await window.api.config.getConfigName()
            for(let i in name){
              if (Object.keys(userConfig.value).length === 0){userConfig.value[name[i]]={};}
              for (let j in userConfigType){
                userConfig.value[name[i]][userConfigType[j]]=JSON.parse(await window.api.config.getConfig(userConfigType[j],name[i]));
              }
            }
      };
      function initGuiConfig(){
        guiConfig.value.selectedConfig=Object.keys(userConfig.value)[0];
        guiConfig.value.server=userConfig.value[guiConfig.value.selectedConfig].config.server;
      }
    
      return{staticConfig,userConfig,guiConfig,getAllConfigs,initGuiConfig}
})