class UserNotFound(Exception):
    def __init__(self, email: str):
        self.message = f"User email {email} not found."
        super().__init__(self.message)

class IncorrectPassword(Exception):
    def __init__(self):
        self.message = "Incorrect password."
        super().__init__(self.message)

