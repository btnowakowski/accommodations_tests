from pytest import mark
from tests.data import generate_test_user
from tests.helpers.auth import register_user, login_user, logout_user, is_user_logged_in


@mark.registration
def test_user_registration(page):
    """Test that new user can register and is automatically logged in."""
    user = generate_test_user()

    register_user(page, user.username, user.email, user.password)

    assert is_user_logged_in(page)


@mark.registration
def test_user_login_after_registration(page):
    """Test that registered user can log out and log back in."""
    user = generate_test_user()

    register_user(page, user.username, user.email, user.password)
    logout_user(page)
    login_user(page, user.username, user.password)

    assert is_user_logged_in(page)
