from pydantic import BaseModel, Field


class User(BaseModel):
    email: str
    password: str = Field(min_length=6, max_length=50)

    # Clase default
    class Config:
        schema_extra = {
            "example": {
                "email": "admin@example.com",
                "password": "P455w.rd"
            }
        }