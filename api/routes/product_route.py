from fastapi import APIRouter

product = APIRouter(prefix="/products")


@product.get("/")
def get_products():
    return {"msg": "Products Route"}


@product.get("/{uuid}")
def get_product(uuid):
    return {"msg": "Product Route", "uuid": uuid}
