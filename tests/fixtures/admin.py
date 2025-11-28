import os
from datetime import datetime, timedelta
import pytest
from tests.data import ADMIN_PANEL, TEST_SERVICE
from tests.helpers.admin import (
    login_admin,
    is_logged_in_admin,
    is_admin_panel_url,
    get_service_heading,
    navigate_to_dashboard,
    navigate_to_slots,
    create_service,
    create_slot,
)


@pytest.fixture
def admin_page(page, base_url):
    """Login to admin panel. Returns page."""
    page.goto(f"{base_url}{ADMIN_PANEL.admin_panel_url_suffix}")
    page.wait_for_load_state("domcontentloaded", timeout=15000)

    if is_admin_panel_url(page) and is_logged_in_admin(page):
        return page

    login_form = page.locator(ADMIN_PANEL.username_input_selector).first
    if login_form.is_visible():
        try:
            login_admin(page, os.getenv("ADMIN_EMAIL"), os.getenv("ADMIN_PASSWORD"))
        except Exception:
            page.screenshot(path="debug_admin_login_failed.png")
            raise

    return page


@pytest.fixture
def admin_page_with_test_service(admin_page):
    """Ensure a test service exists. Returns page."""
    admin_page.goto(admin_page.url + "services/")
    test_service = get_service_heading(admin_page, TEST_SERVICE.name)

    if not test_service.is_visible():
        create_service(
            admin_page,
            TEST_SERVICE.name,
            TEST_SERVICE.description,
            TEST_SERVICE.price,
            TEST_SERVICE.duration,
        )

    return admin_page


@pytest.fixture
def admin_page_with_test_slots(admin_page_with_test_service):
    """Admin page with at least two slots in Test Service. Returns page."""
    admin_page = admin_page_with_test_service
    navigate_to_dashboard(admin_page)
    navigate_to_slots(admin_page)

    slots = admin_page.locator("td", has_text=TEST_SERVICE.name)
    while slots.count() < 2:
        tomorrow = datetime.now() + timedelta(days=1)
        options = admin_page.eval_on_selector_all(
            f"{ADMIN_PANEL.slot_service_select} option",
            "opts => opts.map(o => o.value)",
        )
        last_value = options[-1]
        create_slot(admin_page, last_value, tomorrow.strftime("%Y-%m-%d"))
        slots = admin_page.locator("td", has_text=TEST_SERVICE.name)

    return admin_page
