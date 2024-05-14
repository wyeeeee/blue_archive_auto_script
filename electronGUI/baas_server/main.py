from fastapi import Depends, FastAPI
from electronGUI.baas_server.routers import config
app = FastAPI()
app.include_router(config.router)
@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
