from fastapi import APIRouter
from ..controllers.controller import Controller

home = APIRouter()

homeController = Controller()


@home.get("/")
def get_home():
    return homeController.home_controller()
