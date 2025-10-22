from sqlalchemy.orm import Session

from src.use_cases.get_user_by_email import get_user_by_email_use_case


async def login_user_use_case(email: str, password: str, db_session: Session):
    try:
        user = await get_user_by_email_use_case(email, db_session)
        if not user:
            raise ValueError("User not found.")
        if user.password != password:
            raise ValueError("Incorrect password.")
        return user
    except Exception as e:
        raise e
