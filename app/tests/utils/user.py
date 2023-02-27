import random
import string

from app.schemas.user import UserSignUp


def random_lower_string(len) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=len))


def random_email() -> str:
    return f"{random_lower_string(10)}@{random_lower_string(10)}.com"


def create_mock_signup_user() -> UserSignUp:
    return UserSignUp(
        name=random_lower_string(10),
        surname=random_lower_string(10),
        username=random_lower_string(10),
        email=random_email(),
        password=random_lower_string(32)
    )
