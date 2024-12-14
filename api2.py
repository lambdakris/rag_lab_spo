from fastapi import APIRouter
from msgraph2 import HttpClientDep

router = APIRouter(prefix="/api2")

@router.get("/users")
async def list_users(http_client: HttpClientDep):
    resp = await http_client.get("/users")

    return resp.json().get("value")

@router.get("/sites/all")
async def list_all_sites(http_client: HttpClientDep):
    resp = await http_client.get("/sites")

    return resp.json().get("value")
    
@router.get("/sites/root")
async def list_root_sites(http_client: HttpClientDep):
    resp = await http_client.get("/sites/root")

    return resp.json().get("value")

@router.get("/sites/root/all")
async def list_root_sites(http_client: HttpClientDep):
    resp = await http_client.get("/sites/root/sites")

    return resp.json().get("value")

@router.get("/sites/drives/{site_id}")
async def list_drives(http_client: HttpClientDep, site_id: str):
    drives = await http_client.sites(site_id).drives.get()

    return drives.json().get("value")

@router.get("/sites/drives/files/{drive_id}")
async def list_files(http_client: HttpClientDep, drive_id: str):
    files = await http_client.drives(drive_id).items.get()

    return files