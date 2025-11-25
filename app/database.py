"""Configuration de la base de données et gestion des sessions.

Ce module gère la connexion à la base de données PostgreSQL
et fournit une fonction générateur pour obtenir des sessions de base de données.
"""

from sqlmodel import create_engine, Session
import os
import sys
from typing import Generator

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/items_db"
)

POOL_SIZE = 10

engine = create_engine(DATABASE_URL)


def get_db():
    with Session(engine) as session:
        yield session
