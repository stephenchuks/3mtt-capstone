from fastapi import FastAPI
from app.database import Base, engine
from app.routers import user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router.router)

