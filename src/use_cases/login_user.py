from sqlalchemy.orm import Session

from src.exceptions.user_exceptions import IncorrectPassword, UserNotFound
from src.use_cases.get_user_by_email import get_user_by_email_use_case


async def login_user_use_case(email: str, password: str, db_session: Session):
    user = await get_user_by_email_use_case(email, db_session)
    if not user:
        raise UserNotFound(email=email)
    if user.password != password:
        raise IncorrectPassword()
    return user
