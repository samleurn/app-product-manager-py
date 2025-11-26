from fastapi import APIRouter

home = APIRouter()


@home.get("/")
def get_home():
    return {"msg": "Home route"}
