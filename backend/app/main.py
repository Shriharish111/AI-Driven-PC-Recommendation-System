from fastapi import FastAPI

from app.api.routes import health
from app.core.config import settings
from app.core.logging import setup_logging


def create_app() -> FastAPI:
    setup_logging()

    app = FastAPI(
        title=settings.app_name,
        debug=settings.debug,
    )

    app.include_router(health.router, prefix="/api")

    return app


app = create_app()
