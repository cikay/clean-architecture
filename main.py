from contextlib import asynccontextmanager

from fastapi import FastAPI

from setup_db import setup_db

from routers import discipline
from routers import author
from routers import translator


@asynccontextmanager
async def setup(app: FastAPI):
    setup_db()
    yield


app = FastAPI(lifespan=setup)


app.include_router(discipline.router)
app.include_router(author.router)
app.include_router(translator.router)
