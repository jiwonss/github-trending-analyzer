from fastapi import FastAPI
from app.routers import github

app = FastAPI()

app.include_router(github.router, prefix="/api")
