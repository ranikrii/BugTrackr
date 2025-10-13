from fastapi import FastAPI
from app.db import Base, engine
from app.api.routes import router
from app.models import Base  # make sure models are imported before create_all()

# Initialize FastAPI app
app = FastAPI(title="Bug Tracker")

# Create database tables
Base.metadata.create_all(bind=engine)

# Include all routers (your CRUD routes)
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello! Welcome to Bug Tracker API"}