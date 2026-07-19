from fastapi import FastAPI

from .health_router import router as health_router
from .students_router import router as student_router

def register_api_routes(app: FastAPI):
    app.include_router(health_router, prefix="/api/v1", tags=["Health"])
    app.include_router(student_router, prefix="/api/v1", tags=["Students"])
