from pydantic import BaseModel
from typing import Optional

from src.use_cases.entities.role_enum import RoleEnum

class CreateUserInputDTO(BaseModel):
    email: str
    password: str
    role: RoleEnum
    username: Optional[str] = None
    company_name: Optional[str] = None
    phone_number: Optional[str] = None
    city: Optional[str] = None
    postal_code: Optional[str] = None

class CreateUserResponseDTO(CreateUserInputDTO):
    id: str

class LoginUserInputDTO(BaseModel):
    email: str
    password: str

class LoginUserResponseDTO(CreateUserResponseDTO):
    ...
