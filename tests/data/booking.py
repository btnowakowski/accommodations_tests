from dataclasses import dataclass


@dataclass(frozen=True)
class BookingUIData:
    """
    Booking UI elements, labels and selectors.

    Attributes:
        book_button_role: Book slot button element type
        book_button_text: Book slot button text
        pending_status: Pending reservation status text
        no_slots_message: Message when no slots available
        view_dates_link: Link text to view available dates
        view_dates_link_role: Role for the view dates link
        calendar_selector: CSS selector for calendar
        calendar_placeholder_selector: CSS selector for calendar placeholder
        slot_selector: CSS selector for available slots
        next_week_button_selector: CSS selector for next week button
        slot_preview_selector: CSS selector for slot preview
        slot_event_id_attr: Attribute name for slot event ID
        reservation_card_selector: CSS selector for reservation card
        reservation_meta_selector: CSS selector for reservation meta
        reservation_badge_selector: CSS selector for reservation badge
    """

    # Button and link texts
    book_button_role: str = "button"
    book_button_text: str = "Rezerwuj termin"
    view_dates_link: str = "Zobacz terminy"
    view_dates_link_role: str = "link"

    # Status texts
    pending_status: str = "Oczekująca"
    no_slots_message: str = "Brak terminów w tym tygodniu"

    # Calendar selectors
    calendar_selector: str = "#calendar"
    calendar_placeholder_selector: str = "#calendar-placeholder"
    slot_selector: str = ".fc-event:visible"
    next_week_button_selector: str = ".fc-next-button"
    slot_preview_selector: str = "#slot-preview"
    slot_event_id_attr: str = "data-eventid"

    # Reservation list selectors
    reservation_card_selector: str = ".res-card"
    reservation_meta_selector: str = ".res-meta"
    reservation_badge_selector: str = ".res-badge"


BOOKING_UI = BookingUIData()
