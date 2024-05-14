import aiofiles
import os

async def get_config(config_name,config_type):
    if config_type in ['config','display','event','switch']:
        async with aiofiles.open('./config/{config_name}/{config_type}.json'.format(config_name=config_name,config_type=config_type), 'r',encoding='utf-8') as f:
            config = await f.read()
            return config
    if config_type == 'static':
        async with aiofiles.open('./config/static.json', 'r',encoding='utf-8') as f:
            config = await f.read()
            return config
    return None