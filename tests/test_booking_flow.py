from pytest import mark
from tests.helpers.navigation import navigate_to_my_bookings
from tests.helpers.booking import get_pending_reservations


@mark.booking
def test_user_can_book_slot(page, booked_slot_info: dict):
    """Verify that booking a slot creates a pending reservation."""
    navigate_to_my_bookings(page)

    pending = get_pending_reservations(page)
    assert (
        len(pending) > 0
    ), f"No pending reservations found. Booking info: {booked_slot_info}"

    # Verify booked slot appears in pending reservations
    found = any(
        part in res["full_text"]
        for res in pending
        for part in booked_slot_info["preview_text"].split()
    )
    assert (
        found
    ), f"Booked slot not found in pending reservations. Preview: {booked_slot_info['preview_text']}"
