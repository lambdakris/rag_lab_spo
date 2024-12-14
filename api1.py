from fastapi import APIRouter
from msgraph1 import MsGraphDep

router = APIRouter(prefix="/api1")

@router.get("/users")
async def users(msgraph: MsGraphDep):
    return await msgraph.list_users()

@router.get("/sites")
async def sites(msgraph: MsGraphDep):
    return await msgraph.list_sites()

@router.get("/drives")
async def drives(msgraph: MsGraphDep):
    return await msgraph.list_drives()