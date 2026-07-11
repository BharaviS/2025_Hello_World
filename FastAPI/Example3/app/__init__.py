from fastapi import FastAPI
from .routers import register_api_routes

def create_app():
    app = FastAPI()

    register_api_routes(app)

    return app