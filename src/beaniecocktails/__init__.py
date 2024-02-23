"""
beaniecocktails - A cocktail API built with MongoDB and Beanie
"""
import motor
from beanie import init_beanie
from fastapi import FastAPI
from contextlib import asynccontextmanager

from .models import Cocktail
from .routes import cocktail_router
from .config import Settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    settings = Settings()
    mongodb_url = f"mongodb://{settings.mongo_username}:{settings.mongo_password}@{settings.mongo_server}:{settings.mongo_port}/{settings.mongo_database}"
    client = motor.motor_asyncio.AsyncIOMotorClient(mongodb_url, tls=True)
    await init_beanie(client.get_default_database(), document_models=[Cocktail])
    app.include_router(cocktail_router, prefix="/v1")
    yield
    # shutdown


app = FastAPI(lifespan=lifespan)
