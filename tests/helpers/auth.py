from playwright.sync_api import Page
from tests.data import AUTH_UI


def login_user(page: Page, username: str, password: str):
    """Log in user via login form."""
    page.goto("/")
    page.get_by_role(AUTH_UI.login_link_role, name=AUTH_UI.login_link).click()
    page.locator(AUTH_UI.username_input_selector).fill(username)
    page.get_by_label(AUTH_UI.password_label).fill(password)
    page.get_by_role(AUTH_UI.login_button_role, name=AUTH_UI.login_button).click()
    page.wait_for_load_state("networkidle")


def register_user(page: Page, username: str, email: str, password: str):
    """Register new user via registration form."""
    page.goto("/")
    page.get_by_role(AUTH_UI.register_link_role, name=AUTH_UI.register_link).click()
    page.locator(AUTH_UI.username_input_selector).fill(username)
    page.get_by_label(AUTH_UI.email_label).fill(email)
    page.locator(AUTH_UI.password1_input_selector).fill(password)
    page.locator(AUTH_UI.password2_input_selector).fill(password)
    page.get_by_role(AUTH_UI.register_button_role, name=AUTH_UI.register_button).click()
    page.wait_for_load_state("networkidle")


def logout_user(page: Page):
    """Log out current user."""
    page.get_by_role(AUTH_UI.logout_button_role, name=AUTH_UI.logout_button).click()


def is_user_logged_in(page: Page) -> bool:
    """Check if user is logged in."""
    return page.get_by_role(
        AUTH_UI.my_bookings_link_role, name=AUTH_UI.my_bookings_link
    ).is_visible()
