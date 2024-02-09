from contextlib import asynccontextmanager

from fastapi import FastAPI

from routers import discipline
from models.discipline import DisciplineDB, db


@asynccontextmanager
async def setup(app: FastAPI):
    print("Setting up database")
    db.connect()
    db.create_tables([DisciplineDB])
    yield


app = FastAPI(lifespan=setup)


app.include_router(discipline.router)
