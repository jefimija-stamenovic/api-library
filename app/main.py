from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import app.core.config
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