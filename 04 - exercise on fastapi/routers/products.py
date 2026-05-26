from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter()

class Products(BaseModel):
    item_name: str

@router.get("/", status_code = status.HTTP_200_OK)
async def get_products():
    return {
        "products": ["item 1", "item 2", "item 3"]
    }

@router.post("/create", status_code = status.HTTP_201_CREATED)
async def create_product(product: Products):
    return {
        "item name": product.item_name
    }
