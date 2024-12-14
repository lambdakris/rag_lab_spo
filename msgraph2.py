from typing import Annotated
from pydantic import BaseModel
import httpx
from fastapi import Depends
from settings import GlobalSettingsDep

class Site(BaseModel):
    site_id: str
    site_name: str | None
    site_display: str | None
    web_url: str

class Drive(BaseModel):
    site_id: str
    site_name: str | None
    drive_id: str
    drive_name: str | None
    web_url: str
    drive_type: str

def get_access_token(settings: GlobalSettingsDep):
    url = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
    headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
    data = {
        'grant_type': 'client_credentials',
        'client_id': settings.client_id,
        'client_secret': settings.client_secret,
        'scope': 'https://graph.microsoft.com/.default'
    }
    resp = httpx.post(url, headers=headers, data=data)
    token = resp.json().get("access_token")
    return token

def get_http_client(access_token: str):
    client = httpx.AsyncClient(
        base_url="https://graph.microsoft.com/v1.0", 
        headers={"Authorization": f"Bearer {access_token}"}
    )
    return client

def build_http_client(global_settings: GlobalSettingsDep):
    access_token = get_access_token(global_settings)
    http_client = get_http_client(access_token)
    return http_client
    
HttpClientDep = Annotated[httpx.AsyncClient, Depends(build_http_client)]