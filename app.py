from fastapi import FastAPI, Depends, HTTPException
from state import MsGraphDep

api = FastAPI()

@api.get("/users")
async def users(msgraph: MsGraphDep):
    return await msgraph.list_users()

@api.get("/sites")
async def sites(msgraph: MsGraphDep):
    return await msgraph.list_sites()

@api.get("/drives")
async def drives(msgraph: MsGraphDep):
    return await msgraph.list_drives()