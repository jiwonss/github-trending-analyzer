from fastapi import FastAPI
from app.routers import github
from app.core.database import Base, Engine
import logging
from app.models import repository

app = FastAPI()

app.include_router(github.router, prefix="/api")

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

Base.metadata.drop_all(bind=Engine)
Base.metadata.create_all(bind=Engine)
