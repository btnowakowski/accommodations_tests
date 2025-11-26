# tests/test_admin_panel.py
import os
from pytest import mark, skip
from dotenv import load_dotenv


@mark.admin
def test_admin_panel_dashboard(page, base_url):
    load_dotenv()
    admin_username = os.getenv("ADMIN_EMAIL")
    admin_password = os.getenv("ADMIN_PASSWORD")

    if not admin_username or not admin_password:
        skip("ADMIN_EMAIL / ADMIN_PASSWORD not in env")

    # Logging in as admin
    page.goto("/")
    page.get_by_role("link", name="Zaloguj").click()
    page.locator("input[name='username']").fill(admin_username)
    page.get_by_label("Hasło").fill(admin_password)
    page.get_by_role("button", name="Zaloguj").click()
    page.wait_for_load_state("networkidle")

    # Navigate to admin panel
    page.goto(base_url + "/admin-panel/")
    page.wait_for_load_state("networkidle")

    # Verify admin panel elements
    assert page.locator("div", has_text="Wszystkie").first.is_visible()
    assert page.locator("div", has_text="Oczekujące").first.is_visible()
    assert page.locator("div", has_text="Potwierdzone").first.is_visible()
    assert page.locator("div", has_text="Anulowane").first.is_visible()
