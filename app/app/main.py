from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from core.db import Database

from api.auth import router as router_user
from api.author import router as router_author 
from api.book import router as router_book
from api.base import router

from fastapi.openapi.utils import get_openapi
import uvicorn

def create_app() -> FastAPI: 
    if not getattr(Database, "_engine", None):
        print("LOG ** => 🔧 Database is not initialized, Initialization is next...")
        Database.init(settings)

    app = FastAPI(
        title="Library API",
        description="Welcome to the **Library API** - a RESTful backend server built with **FastAPI**",
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

    app.add_middleware(CORSMiddleware, 
                        allow_origins=["*"], 
                        allow_credentials=True,
                        allow_methods=["*"],
                        allow_headers=["*"])
    app.include_router(router)
    app.include_router(router_user)
    app.include_router(router_author)
    app.include_router(router_book)

    return app

app: FastAPI = create_app()
if __name__ == "__main__":
    import sys, uvicorn

    if "--test" in sys.argv:
        print("🔧 The FastAPI app is running in test mode!")
    elif "--prod" in sys.argv:
        print("🔧 The FastAPI app is running in production mode!")
    else: 
        print("🔧 The FastAPI app is running!")
    
    uvicorn.run("app.main:app", host=settings.APP_HOST, port=settings.APP_PORT, reload=True)