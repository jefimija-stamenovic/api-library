from fastapi import APIRouter
from core.config import settings

router = APIRouter()
@router.get("/", 
         tags=["Welcome"])
def welcome_route() -> dict[str, str]:
    return {
        "message": "Welcome to the API Library — your FastAPI backend is up and running!",
        "swagger_documentation_url": f"http://{settings.APP_HOST}:{settings.APP_PORT}/docs/swagger",
        "redoc_documentation_url": f"http://{settings.APP_HOST}:{settings.APP_PORT}/docs/redoc"
    }