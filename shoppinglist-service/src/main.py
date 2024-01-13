import logging
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.controller import item_routes
from src.database import Base, engine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


logging.basicConfig(level=logging.INFO)

Base.metadata.create_all(bind=engine)

app.include_router(item_routes.router, prefix="/items", tags=["items"])



