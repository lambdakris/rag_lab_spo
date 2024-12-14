from fastapi import FastAPI
import api1
import api2

app = FastAPI()

app.include_router(api1.router)
app.include_router(api2.router)