from fastapi import APIRouter

product = APIRouter()


@product.get("/product")
def get_products():
    return {"msg": "Products Route"}


@product.get("/product/{uuid}")
def get_product(uuid):
    return {"msg": "Product Route", "uuid": uuid}
