from uuid import uuid4, UUID
from pydantic import BaseModel, Field, EmailStr, AnyHttpUrl, SecretStr

class User(BaseModel):
    id: UUID = Field(default_factory=uuid4, description="User ID")
    email: EmailStr = Field(alias="email", description="Email address")
    name: str = Field(alias="name", description="Name of the user")
    age: int = Field(alias="age", description="Age of the user")
    personal_website: AnyHttpUrl | None = Field( alias="personalWebsite", description="Personal website")
    password: SecretStr

if __name__ == "__main__":
    user = User(
        email="test@test.com",
        name="John Doe",
        age=25,
        personalWebsite="https://www.example.com",
        password="test123",
    )
    print(user)              