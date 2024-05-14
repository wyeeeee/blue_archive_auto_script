from fastapi import APIRouter
import json
from electronGUI.baas_server.internal.config_set import get_config as get
router = APIRouter(
    prefix="/get-config",
    tags=["config"],
    responses={404: {"description": "Not found"}},
)
@router.post("/{config_name}/{config_type}")
@router.get("/{config_name}/{config_type}")
async def get_config(config_name,config_type):
    config=await get(config_name,config_type)
    return json.loads(config) if config else None