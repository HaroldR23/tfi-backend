from sqlalchemy.orm import Session

from src.db_models.user import User as UserModel
from src.routes.dtos.user import CreateUserInputDTO
from src.use_cases.get_user_by_email import get_user_by_email_use_case
# from src.db_session import get_db

# db_session = get_db()



async def create_user_use_case(user_dto: CreateUserInputDTO, db_session: Session):
    try:
        user_already_exists = await get_user_by_email_use_case(user_dto.email, db_session)
        if user_already_exists:
            return user_already_exists

        db_user = UserModel(
            username=user_dto.username,
            company_name=user_dto.company_name,
            phone_number=user_dto.phone_number,
            city=user_dto.city,
            postal_code=user_dto.postal_code,
            email=user_dto.email,
            password=user_dto.password,
            role=user_dto.role
        )
        db_session.add(db_user)
        db_session.commit()
        db_session.refresh(db_user)
        
        return db_user
    except Exception as e:
        db_session.rollback()
        raise e
