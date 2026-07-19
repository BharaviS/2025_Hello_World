from fastapi import FastAPI
from .routers import register_api_routes

def create_app(lifespan=None) -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    register_api_routes(app)

    return app