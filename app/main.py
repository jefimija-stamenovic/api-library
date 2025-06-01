from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.auth import router as router_user
from app.api.author import router as router_author 
from app.api.book import router as router_book
from app.core.db import Database

import uvicorn

app = FastAPI(
    title="Library API",
    description="Welcome to the ** Library API** - a RESTful backend server built with **FastAPI**",
    summary="Backend API for managing books, users and authors in a digital library.", 
    version="1.0.0",
    contact={
        "name" : "Jefimija Stamenovic", 
        "url" : "https://github.com/jefimija-stamenovic", 
        "email" : "jefimija.stamenovic@gmail.com"
    },
    license_info={
        "name" : "Apache 2.0", 
        "url" : "https://www.apache.org/licenses/LICENSE-2.0.html"
    }, 
    docs_url="/docs/swagger", 
    redoc_url="/docs/redoc", 
    openapi_url="/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", 
         tags=["Welcome"])
def welcome_route() -> dict[str, str]:
    return {
        "message": "Welcome to the API Library — your FastAPI backend is up and running!",
        "swagger_documentation_url": f"http://{settings.APP_HOST}:{settings.APP_PORT}/docs/swagger",
        "redoc_documentation_url": f"http://{settings.APP_HOST}:{settings.APP_PORT}/docs/redoc"
    }

app.include_router(router_user)
app.include_router(router_author)
app.include_router(router_book)

if __name__ == "__main__":
    Database.init(settings)
    uvicorn.run("app.main:app", host=settings.APP_HOST, port=settings.APP_PORT, reload=True)