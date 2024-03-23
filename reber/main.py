from contextlib import asynccontextmanager

from fastapi import FastAPI

from reber.setup_db import setup_db

from reber.routers import discipline
from reber.routers import author
from reber.routers import book
from reber.routers import interlanguage_discipline


@asynccontextmanager
async def setup(app: FastAPI):
    await setup_db()
    yield


app = FastAPI(lifespan=setup)


app.include_router(interlanguage_discipline.router)
app.include_router(discipline.router)
app.include_router(author.router)
app.include_router(translator.router)
app.include_router(book.router)
