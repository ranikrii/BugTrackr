import sentry_sdk
from fastapi import FastAPI
from app.db import Base, engine
from app.api.routes import router
from app.models import Base  # import models before create_all()
from app.core.config import settings
from app.core.monitoring import init_sentry

app = FastAPI(title="Bug Tracker")

# Creating db table
Base.metadata.create_all(bind=engine)

# Including all routers (CRUD routes)
app.include_router(router)

init_sentry()

@app.get("/")
async def root():
    return {"message": "Hello! Welcome to Bug Tracker API"}

