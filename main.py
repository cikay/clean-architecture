from contextlib import asynccontextmanager

from fastapi import FastAPI
from models.author import AuthorDB

from routers import discipline
from routers import author
from models.base import db
from models.discipline import DisciplineDB


@asynccontextmanager
async def setup(app: FastAPI):
    print("Setting up database")
    db.connect()
    db.create_tables([DisciplineDB, AuthorDB])
    yield


app = FastAPI(lifespan=setup)


app.include_router(discipline.router)
app.include_router(author.router)
