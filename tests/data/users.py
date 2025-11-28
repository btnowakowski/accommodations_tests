import time
import random
import string
from dataclasses import dataclass


@dataclass(frozen=True)
class UserCredentials:
    """
    User credentials for authentication tests.

    Attributes:
        username: User's login name
        email: User's email address
        password: User's password
    """

    username: str
    email: str
    password: str


def generate_test_user() -> UserCredentials:
    """
    Generate random test user credentials.

    Returns:
        UserCredentials with unique username, email and default password.
    """
    stamp = int(time.time())
    rand = "".join(random.choices(string.ascii_lowercase, k=5))
    email = f"test_{rand}_{stamp}@example.com"
    return UserCredentials(
        username=email.split("@")[0],
        email=email,
        password="Test1234!abcd",
    )
