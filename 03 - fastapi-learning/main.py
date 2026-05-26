from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def home():
    return {
        "message": "Hello FastAPI"
    }

@app.get("/about")
async def about():
    return {
        "framework": "FastAPI",
        "language": "Python"
    }

@app.get("/users/{name}")
async def get_username(name: str):
    return {
        "user": name
    }

@app.get("/search")
async def get_query_params(q: str):
    return {
        "query": q
    }

@app.get("/dummy/{name}")
async def get_query_path_param(q: str, name: str):
    return {
        "name": name,
        "query": q
    }

# Exercise 1 — Create Pydantic model
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    is_admin: bool
    city: str | None = None

# @app.post("/users")
# async def create_user(user: User):
#     return {
#         "message": "user created successfully!",
#         "name": user.name,
#         "city": user.city
#     }

class UserResponse(BaseModel):
    name: str
    age:  int

@app.post("/users", response_model=UserResponse)
async def create_user(user: User):
    return user


# Returning proper status codes with messages:
# Exercise 1 — Proper status and Error handling
from fastapi import status, HTTPException

@app.post("/create-user/{id}", status_code=status.HTTP_201_CREATED)
async def create_user(id: int):
    if id != 1:
        raise HTTPException(
            status_code = 404,
            detail = "User not found"
        )
    
    return {
        "id": id,
        "name": "xyz"
    }

# Exercise 3 — Query validation
@app.get("/items", status_code=status.HTTP_200_OK)
async def get_items(limit: int):

    return {
        "limit": limit
    }

# Exercise 4 — Optional query params
@app.get("/item-details", status_code=status.HTTP_200_OK)
async def get_items(search: str | None = None):

    return {
        "search": search
    }

# Exercise 5 — Combine everything
@app.get("/user-id/{id}", status_code=status.HTTP_200_OK)
async def get_id(id: int, search: str | None = None):

    if id != 1:
        raise HTTPException(
            status_code = 404,
            detail = "Invalid user id"
        )
    
    return {
        "id": id
    }