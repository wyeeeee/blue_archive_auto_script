import fs from 'fs';
import path from 'path';
const configService = {
    name: 'config',
    fns: {
        async getConfig(type,name=null) {
          try{
          if(type=='static'){
            const data = fs.readFileSync(`../config/${type}.json`, 'utf8');
            return data;
          }
        }catch{
            return false;
          }
            if (fs.existsSync(`../config/${name}`)) {
                try{
                    const data = fs.readFileSync(`../config/${name}/${type}.json`, 'utf8');
                    return data;
                }catch{
                    return false;
                }
              } else {
                return false;
              }
      },
      async getConfigName(){
        return fs.readdirSync('../config').filter(file => fs.statSync(path.join('../config', file)).isDirectory())
      }
    }
  };
  
  export default configService;