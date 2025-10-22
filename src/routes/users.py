from fastapi import APIRouter, Depends
from src.db_session import get_db

from src.routes.dtos.user import (
    CreateUserInputDTO, 
    CreateUserResponseDTO, 
    LoginUserInputDTO, 
    LoginUserResponseDTO,
    ResetPasswordInputDTO
)
from src.use_cases.create_user import create_user_use_case
from src.use_cases.login_user import login_user_use_case
from src.use_cases.reset_password import reset_password_use_case

user_router = APIRouter()

@user_router.post("/signup", response_model=CreateUserResponseDTO)
async def signup(
        user: CreateUserInputDTO, 
        db_session=Depends(get_db)
    ):
    try:
        created_user = await create_user_use_case(
            user_dto=user, 
            db_session=db_session
        )
        return CreateUserResponseDTO(
            city=created_user.city,
            company_name=created_user.company_name,
            email=created_user.email,
            id=str(created_user.id),
            password=created_user.password,
            phone_number=created_user.phone_number,
            postal_code=created_user.postal_code,
            role=created_user.role,
            username=created_user.username
        )
    except Exception as e:
        raise e


@user_router.post("/login", response_model=LoginUserResponseDTO)
async def login(request_data: LoginUserInputDTO, db_session=Depends(get_db)):
    try:
        response = await login_user_use_case(
            email=request_data.email,
            password=request_data.password,
            db_session=db_session
        )
        return LoginUserResponseDTO(
            city=response.city,
            company_name=response.company_name,
            email=response.email,
            id=str(response.id),
            password=response.password,
            phone_number=response.phone_number,
            postal_code=response.postal_code,
            role=response.role,
            username=response.username
        )
    except Exception as e:
        raise e 
    
@user_router.post("/reset-password")
async def reset_password(request_data: ResetPasswordInputDTO, db_session=Depends(get_db)):
    try:
        response = await reset_password_use_case(
            email=request_data.email,
            new_password=request_data.new_password,
            db_session=db_session
        )
        return response
    except Exception as e:
        raise e
