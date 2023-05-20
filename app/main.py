# FastAPI
from fastapi import FastAPI

from api import get_question
from api import registration
from api import media
from models.db import engine, database, metadata

# Metrics
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi.middleware.cors import CORSMiddleware

metadata.create_all(engine)
app = FastAPI(title='Test app')
app.include_router(get_question.router)
app.include_router(registration.router)
app.include_router(media.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Instrumentator().instrument(app).expose(app)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/')
async def get_main_page():
    return "Hello world!"
