import { contextBridge,ipcRenderer } from 'electron'
import { electronAPI } from '@electron-toolkit/preload'
import { services, makeChannelName } from '../main/services';
// Custom APIs for renderer
function createJsBridge() {
  const bridge = {};

  services.forEach((service) => {
    bridge[service.name] = {};

    Object.keys(service.fns).forEach((fnName) => {
      bridge[service.name][fnName] = (...args) =>
        ipcRenderer.invoke(makeChannelName(service.name, fnName), ...args);
    });
  });
  return bridge;
}
// Use `contextBridge` APIs to expose Electron APIs to
// renderer only if context isolation is enabled, otherwise
// just add to the DOM global.
if (process.contextIsolated) {
  try {
    contextBridge.exposeInMainWorld('electron', electronAPI)
    contextBridge.exposeInMainWorld('setWin', {min:()=>ipcRenderer.send('min'),max:()=>ipcRenderer.send('max'),close:()=>ipcRenderer.send('close')})
    contextBridge.exposeInMainWorld('api',  createJsBridge());
  } catch (error) {
    console.error(error)
  }
} else {
  window.electron = electronAPI
  window.api = api
}
