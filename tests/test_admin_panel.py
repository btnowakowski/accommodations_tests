from pytest import mark, skip
from tests.data import ADMIN_PANEL, TEST_SERVICE
from tests.helpers import (
    get_stat_cards,
    get_stat_dots,
    get_stat_card_by_label,
    get_stat_count,
    is_admin_panel_url,
    get_pending_reservations_list,
    get_pending_reservation_items,
    has_no_pending_reservations_message,
    verify_reservation_item_structure,
    get_service_heading,
    get_slots,
)


@mark.admin
def test_admin_panel_loads(admin_page):
    """Admin login and panel load verification - prerequisite for other tests"""
    assert is_admin_panel_url(admin_page), "Admin panel URL not correct"
    assert get_stat_dots(admin_page).count() > 0, "Admin panel content not loaded"


@mark.admin
def test_admin_panel_stat_cards_visible(admin_page):
    """Verify all stat cards are visible"""
    stat_cards = get_stat_cards(admin_page)
    assert (
        stat_cards.count() >= ADMIN_PANEL.min_stat_cards
    ), "Should have at least 4 stat cards"

    for label in ADMIN_PANEL.stat_labels:
        card = get_stat_card_by_label(admin_page, label)
        assert card.is_visible(), f"Card '{label}' not visible"


@mark.admin
def test_admin_panel_reservation_numbers_are_numeric(admin_page):
    """Verify reservation numbers are valid"""
    stat_cards = get_stat_cards(admin_page)

    for i in range(stat_cards.count()):
        get_stat_count(stat_cards.nth(i))  # Raises AssertionError if invalid


@mark.admin
def test_admin_panel_stat_dots_visible(admin_page):
    """Verify status indicators are visible"""
    stat_dots = get_stat_dots(admin_page)
    assert stat_dots.count() >= 1, "Should have status indicators"

    for i in range(stat_dots.count()):
        assert stat_dots.nth(i).is_visible(), f"Status indicator #{i} is not visible"


@mark.admin
def test_admin_panel_pending_reservations_list(admin_page):
    """Verify pending reservations list structure"""
    pending_list = get_pending_reservations_list(admin_page)

    if not pending_list.is_visible():
        skip("Pending reservations list not visible")

    reservation_items = get_pending_reservation_items(admin_page)

    if reservation_items.count() == 0:
        assert has_no_pending_reservations_message(
            admin_page
        ), f"Expected '{ADMIN_PANEL.no_pending_message}' message"
        skip("No pending reservations available")

    # Check first reservation item structure
    first_item = reservation_items.first
    elements = verify_reservation_item_structure(first_item)

    assert elements["user_service"].is_visible(), "User and service name not visible"
    assert elements["has_arrow"], "Should contain arrow separator"
    assert elements["timestamp"].is_visible(), "Timestamp not visible"
    assert elements["approve_button"].is_visible(), "Approve button not visible"
    assert elements["reject_button"].is_visible(), "Reject button not visible"


@mark.admin
def test_admin_can_create_service(admin_page_with_test_service):
    """Verify admin can create a test service"""
    heading = get_service_heading(admin_page_with_test_service, TEST_SERVICE.name)
    assert heading.is_visible(), "Test service not found"


@mark.admin
def test_admin_can_create_slots(admin_page_with_test_slots, base_url):
    """Verify admin can create test slots"""
    admin_page_with_test_slots.goto(f"{base_url}{ADMIN_PANEL.slots_url_suffix}")
    admin_page_with_test_slots.wait_for_load_state("networkidle")

    slots = get_slots(admin_page_with_test_slots)
    assert slots.count() > 0, "No slots found"
