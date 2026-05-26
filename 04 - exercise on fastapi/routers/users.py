from fastapi import APIRouter, status
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

router = APIRouter()

@router.get("/", status_code = status.HTTP_200_OK)
async def get_users():
    return {
        "users": ["Omkar", "Rahul", "Vinit"]
    }

@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):

    # My question here is how do we nicely return the error if it's invalid, I know pydantic handles it, but it does look ugly, how should frontend handle the error part?
    # For example when input is incorrect it provides this response: how should this be handled in the frontend:
    """
    {
        "detail": [
            {
                "type": "int_parsing",
                "loc": [
                    "body",
                    "age"
                ],
                "msg": "Input should be a valid integer, unable to parse string as an integer",
                "input": "int"
            }
        ]
    }
    """
    return {
        "message": "User created successfully",
        "name": user.name,
        "age": user.age
    }