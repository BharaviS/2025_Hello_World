from fastapi import FastAPI
from contextlib import asynccontextmanager
from uvicorn import run
from app import create_app
from app.database import init_db

# TODO: creating DataBase
@asynccontextmanager
async def lifespan(_app: FastAPI):
    await init_db()
    yield

app = create_app(lifespan=lifespan)

if __name__ == '__main__':
    run("main:app", host="0.0.0.0", port=8000, reload=True)