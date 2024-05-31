import { defineStore } from 'pinia'

export const useConfigStore = defineStore('config', {
  state: () => {
    return { 
      staticConfig:null,
      userConfig:[],
    }
  },
  actions: {
    increment() {
    },
  },
})