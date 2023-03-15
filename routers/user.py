from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas.user import User
from utils.jwt_manager import create_token

user_router = APIRouter()

@user_router.post("/login", tags=["auth"])
def login(user: User):
    if user.email == "admin@example.com" and user.password == "P455w.rd":
        token: str = create_token(user.dict()) # Convierto el usuer a un dict
        return JSONResponse(status_code=200, content=token)