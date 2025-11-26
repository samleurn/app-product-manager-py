from fastapi import APIRouter
from .home_route import home
from .product_route import product

router = APIRouter(prefix="/api")

router.include_router(home)
router.include_router(product)
