import fs from 'fs';
const configService = {
    name: 'config',
    fns: {
        async getConfig(name,type) {

            if (fs.existsSync(`../config/${name}`)) {
                try{
                  if(type=='static'){
                    const data = fs.readFileSync(`../config/${type}.json`, 'utf8');
                    return data;
                  }
                    const data = fs.readFileSync(`../config/${name}/${type}.json`, 'utf8');
                    return data;
                }catch{
                    return false;
                }
              } else {
                return false;
              }
      } 
    }
  };
  
  export default configService;