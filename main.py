from contextlib import asynccontextmanager

from fastapi import FastAPI

from routers import subject
from models.subject import SubjectDB, db


@asynccontextmanager
async def setup(app: FastAPI):
    print("Setting up database")
    db.connect()
    db.create_tables([SubjectDB])
    yield


app = FastAPI(lifespan=setup)


app.include_router(subject.router)
