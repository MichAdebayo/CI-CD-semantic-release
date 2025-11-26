from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import SQLModel
from app.database import engine
from app.routes import items_router
import os
from typing import AsyncGenerator

# Initialize central logging as early as possible so module logs go into the
# project `logs/app.log` file (rotating).
from app.logging_config import setup_logging

setup_logging()

DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() in ("true", "1", "t")


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI) -> AsyncGenerator[None, None]:
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(
    title="Items CRUD API",
    description="API pour gérer une liste d'articles",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(items_router)


@app.get("/")
def root() -> dict:
    return {"message": "Items CRUD API"}


@app.get("/health")
def health() -> dict:
    return {"status": "healthy"}
