from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def index():
    return {"message": "Server health is running"}