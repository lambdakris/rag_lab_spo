from typing import Annotated
from fastapi import Depends
from pydantic import BaseModel
from pydantic_settings import BaseSettings

class GlobalSettings(BaseSettings):
    tenant_id: str = None
    client_id: str = None
    client_secret: str = None
    
async def get_global_settings():
    return GlobalSettings(_env_file=".env") 

GlobalSettingsDep = Annotated[GlobalSettings, Depends(get_global_settings)]