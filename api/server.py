from fastapi import FastAPI
from .routes.home import home
from .routes.product import product

app = FastAPI()

app.include_router(home, prefix="/api")
app.include_router(product, prefix="/api")
