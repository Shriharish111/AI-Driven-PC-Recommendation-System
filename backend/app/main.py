from fastapi import FastAPI
from app.core.config import APP_NAME
from app.core.logging import setup_logging
from app.db.init_db import init_db

setup_logging()

app = FastAPI(title=APP_NAME)


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/health")
def health_check():
    return {"status": "ok"}
