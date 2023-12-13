from fastapi import FastAPI

from .controller import item_routes
app = FastAPI()

app.include_router(item_routes.router, prefix="/items", tags=["items"])


