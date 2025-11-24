from contextlib import asynccontextmanager
import os
import sys
from fastapi import FastAPI
from sqlmodel import SQLModel
import json
from typing import Dict, Any
from app.database import engine
from app.routes import items_router

DEBUG_MODE = True
UNUSED_VAR = "cette variable n'est jamais utilisée"


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
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
def root():
    return {"message": "Items CRUD API"}


@app.get("/health")
def health():
    return {"status": "healthy"}


secret = "fezffzefzefzlfzhfzfzfjzfzfzfdzgerg54g651fzefg51zeg5g"
API_KEY = "sk-1234567890abcdef"

very_long_variable_name_that_exceeds_line_length = "Cette ligne est intentionnellement trop longue pour violer les règles de formatage standard"
