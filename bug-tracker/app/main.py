from fastapi import FastAPI
from app.db import Base, engine
from app.api.routes import router
from app.models import Base  # import models before create_all()

app = FastAPI(title="Bug Tracker")

# Creating db table
Base.metadata.create_all(bind=engine)

# Including all routers (CRUD routes)
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello! Welcome to Bug Tracker API"}