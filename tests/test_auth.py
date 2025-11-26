import time
import random
import string
from pytest import mark


def random_email():
    stamp = int(time.time())
    rand = "".join(random.choices(string.ascii_lowercase, k=5))
    return f"test_{rand}_{stamp}@example.com"


@mark.registration
def test_registration_and_login(page):
    email = random_email()
    password = "Test1234!abcd"
    username = email.split("@")[0]

    # Registration flow
    page.goto("/")
    page.get_by_role("link", name="Rejestracja").click()

    page.locator("input[name='username']").fill(username)

    page.get_by_label("Email").fill(email)

    page.locator("input[name='password1']").fill(password)
    page.locator("input[name='password2']").fill(password)

    page.get_by_role("button", name="Załóż konto").click()

    page.wait_for_load_state("networkidle")

    # Verify successful registration and automatic login
    assert page.get_by_role("link", name="Moje rezerwacje").is_visible()

    page.get_by_role("button", name="Wyloguj").click()

    # Login flow
    page.get_by_role("link", name="Zaloguj").click()

    page.locator("input[name='username']").fill(username)
    page.get_by_label("Hasło").fill(password)
    page.get_by_role("button", name="Zaloguj").click()

    page.wait_for_load_state("networkidle")

    # Verify successful login
    assert page.get_by_role("link", name="Moje rezerwacje").is_visible()
