from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from http import HTTPStatus

from src.exceptions.user_exceptions import IncorrectPassword, UserNotFound


def register_exception_handler(app: FastAPI):

    @app.exception_handler(UserNotFound)
    async def user_not_found_exception_handler(request: Request, exc: UserNotFound):
        return JSONResponse(
            status_code=HTTPStatus.NOT_FOUND,
            content={"message": exc.message}
        )

    @app.exception_handler(IncorrectPassword)
    async def incorrect_password_exception_handler(request: Request, exc: IncorrectPassword):
        return JSONResponse(
            status_code=HTTPStatus.UNAUTHORIZED,
            content={"message": exc.message}
        )
    