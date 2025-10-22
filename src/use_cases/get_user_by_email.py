
from sqlalchemy.orm import Session

from src.db_models.user import User as UserModel
from src.routes.dtos.user import CreateUserInputDTO

async def get_user_by_email_use_case(email: str, db_session: Session):
    try:
        user = db_session.query(UserModel).filter(UserModel.email == email).first()
        return user
    except Exception as e:
        return None
