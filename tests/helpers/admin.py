from playwright.sync_api import Page
from tests.data import ADMIN_PANEL


def login_admin(page: Page, username: str, password: str):
    """Login to admin panel."""
    page.fill(ADMIN_PANEL.username_input_selector, username)
    page.fill(ADMIN_PANEL.password_input_selector, password)
    page.get_by_role("button", name=ADMIN_PANEL.login_button_text).click()
    page.wait_for_url(f"**{ADMIN_PANEL.admin_panel_url_suffix}**", timeout=15000)
    page.wait_for_load_state("networkidle")


def is_logged_in_admin(page: Page) -> bool:
    """Check if admin is already logged in."""
    return get_stat_cards(page).count() > 0


def navigate_to_dashboard(page: Page):
    """Navigate to admin dashboard."""
    page.get_by_role("link", name=ADMIN_PANEL.dashboard_link).first.click()
    page.wait_for_load_state("networkidle")


def navigate_to_slots(page: Page):
    """Navigate to slots management."""
    page.get_by_role("link", name=ADMIN_PANEL.slots_link).first.click()
    page.wait_for_load_state("networkidle")


def create_service(page: Page, name: str, description: str, price: str, duration: str):
    """Create a new service."""
    page.get_by_role("link", name=ADMIN_PANEL.add_service_link).click()
    page.wait_for_load_state("networkidle")
    page.fill(ADMIN_PANEL.service_name_input, name)
    page.fill(ADMIN_PANEL.service_description_input, description)
    page.fill(ADMIN_PANEL.service_price_input, price)
    page.fill(ADMIN_PANEL.service_duration_input, duration)
    page.get_by_role("button", name=ADMIN_PANEL.save_button_text).click()
    page.wait_for_load_state("networkidle")


def create_slot(page: Page, service_value: str, date_str: str, time_index: int = 2):
    """Create a new slot for service."""
    page.get_by_role("link", name=ADMIN_PANEL.add_slot_link).click()
    page.wait_for_load_state("networkidle")
    page.select_option(ADMIN_PANEL.slot_service_select, value=service_value)
    page.fill(ADMIN_PANEL.slot_date_input, date_str)
    page.wait_for_timeout(500)
    page.select_option(ADMIN_PANEL.slot_time_select, index=time_index)
    page.get_by_role("button", name=ADMIN_PANEL.save_button_text).click()
    page.wait_for_load_state("networkidle")


def get_stat_cards(page: Page):
    """Get all stat cards locator."""
    return page.locator(ADMIN_PANEL.stat_card_selector)


def get_stat_dots(page: Page):
    """Get all stat dots locator."""
    return page.locator(ADMIN_PANEL.stat_dot_selector)


def get_stat_card_by_label(page: Page, label: str):
    """Get stat card by its label text."""
    return get_stat_cards(page).filter(has_text=label).first


def get_stat_count(stat_card) -> int:
    """Extract numeric count from stat card. Raises AssertionError if not numeric."""
    count_text = stat_card.locator(ADMIN_PANEL.stat_count_selector).inner_text()
    try:
        count = int(count_text)
        assert count >= 0, f"Reservation count should not be negative: {count}"
        return count
    except ValueError:
        raise AssertionError(f"Value '{count_text}' is not a number")


def is_admin_panel_url(page: Page) -> bool:
    """Check if current URL is admin panel."""
    return page.url.endswith(ADMIN_PANEL.admin_panel_url_suffix)


def get_pending_reservations_list(page: Page):
    """Get pending reservations list locator."""
    return page.locator(ADMIN_PANEL.pending_list_selector).first


def get_pending_reservation_items(page: Page):
    """Get all pending reservation items."""
    pending_list = get_pending_reservations_list(page)
    return pending_list.locator(ADMIN_PANEL.pending_item_selector)


def has_no_pending_reservations_message(page: Page) -> bool:
    """Check if 'no pending reservations' message is visible."""
    return (
        page.locator(ADMIN_PANEL.no_pending_selector).is_visible()
        or page.locator(f"text={ADMIN_PANEL.no_pending_message}").is_visible()
    )


def verify_reservation_item_structure(item) -> dict:
    """Verify reservation item has required elements. Returns dict with elements."""
    user_service = item.locator(ADMIN_PANEL.user_service_selector)
    timestamp = item.locator(ADMIN_PANEL.timestamp_selector)
    approve_btn = item.locator(ADMIN_PANEL.approve_button_selector)
    reject_btn = item.locator(ADMIN_PANEL.reject_button_selector)

    return {
        "user_service": user_service,
        "timestamp": timestamp,
        "approve_button": approve_btn,
        "reject_button": reject_btn,
        "has_arrow": ADMIN_PANEL.arrow_separator in user_service.inner_text(),
    }


def get_service_heading(page: Page, service_name: str):
    """Get service heading by name."""
    return page.locator(ADMIN_PANEL.service_heading_selector, has_text=service_name)


def get_slots(page: Page):
    """Get all slots on slots page."""
    return page.locator(ADMIN_PANEL.slot_item_selector)
