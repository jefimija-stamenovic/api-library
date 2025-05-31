from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from app.api.routes import router as api_router  # Импорт целог API entrypoint-а

app = FastAPI(
    title="Biblioteka API",
    description="REST API za upravljanje bibliotekom",
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
    allow_origins=["*"],  # Промени у production-у ако треба
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
def ping() -> dict[str, str]:
    return {"message": "Server uspešno radi!"}

if __name__ == "__main__": 
    import uvicorn
    from app.core.db import Database
    from app.core.config import settings

    db : Database = Database(settings=settings)
    uvicorn.run("app.main:app", host=settings.APP_HOST, port=settings.APP_PORT, reload=True)