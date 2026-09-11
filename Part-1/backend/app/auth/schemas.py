from pydantic import BaseModel, EmailStr, Field

class AuthCredentials(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)

class UserOut(BaseModel):
    id: int
    email: EmailStr
    class Config:
        from_attributes = True

class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut

class ProfileIn(BaseModel):
    full_name: str = Field(default="", max_length=120)
    phone: str = Field(default="", max_length=30)
    branch: str = Field(default="", max_length=120)
    education_level: str = Field(default="", max_length=80)
    college: str = Field(default="", max_length=180)
    graduation_year: int | None = None
    target_career: str = Field(default="", max_length=160)
    bio: str = Field(default="", max_length=1000)

class ProfileOut(ProfileIn):
    user_id: int
    email: EmailStr
    class Config:
        from_attributes = True
