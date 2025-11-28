from playwright.sync_api import Page
from tests.data import AUTH_UI, BOOKING_UI, TEST_SERVICE


def navigate_to_services(page: Page):
    """Navigate to services page."""
    services_link = page.get_by_role(
        TEST_SERVICE.services_link_role, name=TEST_SERVICE.services_link
    )
    services_link.wait_for(state="visible")
    services_link.click()
    page.wait_for_load_state("networkidle")


def select_first_service(page: Page):
    """Select the first service from the list."""
    first_service_link = page.get_by_role(
        BOOKING_UI.view_dates_link_role, name=BOOKING_UI.view_dates_link
    ).first
    first_service_link.wait_for(state="visible")
    first_service_link.click()
    page.wait_for_load_state("networkidle")


def navigate_to_my_bookings(page: Page):
    """Navigate to 'My Reservations' page."""
    my_bookings_link = page.get_by_role(
        AUTH_UI.my_bookings_link_role, name=AUTH_UI.my_bookings_link
    )
    my_bookings_link.wait_for(state="visible")
    my_bookings_link.click()
    page.wait_for_load_state("networkidle")
