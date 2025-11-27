from fastapi import APIRouter
from ..controllers.controller import Controller

product = APIRouter(prefix="/products")

productController = Controller()


@product.get("/")
def get_products():
    return productController.product_controller("/getall")


@product.get("/{uuid}")
def get_product(uuid):
    return productController.product_controller("/getone", uuid)
