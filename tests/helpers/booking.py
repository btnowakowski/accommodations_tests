from playwright.sync_api import Page
from tests.data import BOOKING_UI


def find_available_slot(page: Page, max_weeks: int = 5):
    """Find first available slot in calendar. Returns locator or None."""
    calendar = page.locator(BOOKING_UI.calendar_selector)
    if not calendar.is_visible():
        placeholder = page.locator(BOOKING_UI.calendar_placeholder_selector)
        if placeholder.get_by_text(BOOKING_UI.no_slots_message).is_visible():
            return None
        raise AssertionError("Neither calendar nor 'no slots' placeholder is visible.")

    calendar.wait_for(state="visible")

    for _ in range(max_weeks):
        free_slots = page.locator(BOOKING_UI.slot_selector)
        if free_slots.count() > 0:
            return free_slots.first
        next_week_button = page.locator(BOOKING_UI.next_week_button_selector)
        next_week_button.click()
        page.wait_for_timeout(500)

    return None


def book_slot(page: Page, slot_locator) -> dict:
    """Book the selected slot. Returns dict with booking info."""
    slot_locator.wait_for(state="visible")
    slot_id = slot_locator.get_attribute(BOOKING_UI.slot_event_id_attr)
    slot_text = slot_locator.inner_text().strip()

    slot_locator.click()
    page.wait_for_timeout(300)

    slot_preview = page.locator(BOOKING_UI.slot_preview_selector)
    slot_preview.wait_for(state="visible")
    slot_preview_text = slot_preview.inner_text().strip()

    book_button = page.get_by_role(
        BOOKING_UI.book_button_role, name=BOOKING_UI.book_button_text
    )
    book_button.wait_for(state="visible")
    book_button.click()
    page.wait_for_load_state("networkidle")

    return {
        "slot_id": slot_id,
        "slot_text": slot_text,
        "slot_label": slot_id or slot_text,
        "preview_text": slot_preview_text,
    }


def get_reservations(page: Page) -> list[dict]:
    """Get list of reservations from 'My Reservations' page."""
    rows = page.locator(BOOKING_UI.reservation_card_selector)
    if rows.count() == 0:
        return []
    rows.first.wait_for(state="visible")

    matched = page.locator(f"{BOOKING_UI.reservation_card_selector}:visible")
    count = matched.count()

    reservations = []
    for i in range(count):
        res_meta = (
            matched.locator(BOOKING_UI.reservation_meta_selector).nth(i).inner_text()
        )
        res_badge = (
            matched.locator(BOOKING_UI.reservation_badge_selector).nth(i).inner_text()
        )
        reservations.append(
            {
                "index": i,
                "meta": res_meta,
                "status": res_badge,
                "full_text": matched.nth(i).inner_text(),
            }
        )
    return reservations


def get_pending_reservations(page: Page) -> list[dict]:
    """Get only pending reservations."""
    reservations = get_reservations(page)
    return [r for r in reservations if BOOKING_UI.pending_status in r["status"]]
