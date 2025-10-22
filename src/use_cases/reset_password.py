from sqlalchemy.orm import Session

from .get_user_by_email import get_user_by_email_use_case

async def reset_password_use_case(
		email: str,
		new_password: str,
		db_session: Session
	):
		user = await get_user_by_email_use_case(email, db_session)
		if not user:
			raise Exception("User not found")

		user.password = new_password

		db_session.commit()
		db_session.refresh(user)

		return {"message": "Password reset successful"}
