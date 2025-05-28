from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from app.api.routes import router as api_router  # Импорт целог API entrypoint-а

app = FastAPI(
    title="Biblioteka API",
    description="REST API za upravljanje bibliotekom",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Промени у production-у ако треба
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Увезујемо све руте из API слоја
#app.include_router(api_router)

# Healthcheck рутa
@app.get("/ping")
def ping() -> dict[str, str]:
    return {"message": "pong 🏓"}

if __name__ == "__main__": 
    import uvicorn
    from app.core.config import settings

    uvicorn.run("app.main:app", host=settings.APP_HOST, port=settings.APP_PORT, reload=True)