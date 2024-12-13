from typing import Annotated
from pydantic import BaseModel
from fastapi import Depends
from azure.identity.aio import ClientSecretCredential
from msgraph import GraphServiceClient
from msgraph.generated.users.users_request_builder import UsersRequestBuilder
from msgraph.generated.sites.sites_request_builder import SitesRequestBuilder
from msgraph.generated.drives.drives_request_builder import DrivesRequestBuilder
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

class MsGraph:
    credential: ClientSecretCredential
    client: GraphServiceClient

    def __init__(self, settings: GlobalSettingsDep):
        self.credentials = ClientSecretCredential(
            settings.tenant_id, 
            settings.client_id, 
            settings.client_secret
        )
        self.client = GraphServiceClient(self.credentials)

    async def list_users(self):
        resp = await self.client.users.get()

        return resp.value
    
    async def list_sites(self):
        resp = await self.client.sites.get()

        return [
            Site(
                site_id = site.id,
                site_name = site.name,
                site_display = site.display_name,
                web_url = site.web_url
            )
            for site in resp.value
        ]
    
    async def list_drives(self):
        aggr : list[Drive] = []

        sites = await self.client.sites.get()
        for site in sites.value:
            drives = await self.client.sites.by_site_id(site.id).drives.get()
            for drive in drives.value:
                if drive.drive_type == "documentLibrary":
                    aggr.append(
                        Drive(
                            site_id = site.id,
                            site_name = site.name,
                            drive_id = drive.id,
                            drive_name = drive.name,
                            web_url = drive.web_url,
                            drive_type = drive.drive_type
                        )
                    )

        return aggr
    
MsGraphDep = Annotated[MsGraph, Depends(MsGraph)]