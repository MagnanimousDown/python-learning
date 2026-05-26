from fastapi import FastAPI
from routers.users import router as user_router
from routers.products import router as product_router

app = FastAPI()

app.include_router(user_router, prefix = "/users", tags = ["Users"])
app.include_router(product_router, prefix = "/products", tags = ["Products"])