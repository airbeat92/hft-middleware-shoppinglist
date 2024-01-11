import logging
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from controller import item_routes
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


logging.basicConfig(level=logging.INFO)


app.include_router(item_routes.router, prefix="/items", tags=["items"])



