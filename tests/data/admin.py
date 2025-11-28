from dataclasses import dataclass


@dataclass(frozen=True)
class AdminPanelData:
    """
    Admin panel expected content and configuration.

    Attributes:
        stat_labels: Labels for statistics cards
        min_stat_cards: Minimum expected number of stat cards
        no_pending_message: Message when no pending reservations

    Selectors:
        stat_card_selector: CSS selector for stat cards
        stat_dot_selector: CSS selector for status indicators
        stat_count_selector: CSS selector for count in stat card
        pending_list_selector: CSS selector for pending reservations list
        pending_item_selector: CSS selector for pending reservation item
        user_service_selector: CSS selector for user/service info
        timestamp_selector: CSS selector for timestamp
        approve_button_selector: CSS selector for approve button
        reject_button_selector: CSS selector for reject button

    Navigation:
        admin_panel_link: Admin panel link text
        admin_panel_link_role: Admin panel link element role
        admin_panel_url_suffix: Expected URL suffix for admin panel
    """

    # Stats configuration
    stat_labels: tuple[str, ...] = (
        "Wszystkie",
        "Potwierdzone",
        "Anulowane",
        "Oczekujące",
    )
    min_stat_cards: int = 4

    # Messages
    no_pending_message: str = "Brak oczekujących rezerwacji"

    # Stat card selectors
    stat_card_selector: str = ".stat-card"
    stat_dot_selector: str = ".stat-dot"
    stat_count_selector: str = ".fs-4"

    # Pending reservations selectors
    pending_list_selector: str = "ul.mb-0, [data-testid='pending-reservations-list']"
    pending_item_selector: str = "li.py-2"
    user_service_selector: str = ".fw-semibold"
    timestamp_selector: str = ".text-muted-2.small"
    approve_button_selector: str = "a.btn-success"
    reject_button_selector: str = "a.btn-outline-danger"
    no_pending_selector: str = "[data-testid='no-pending-reservations']"

    # Navigation
    admin_panel_link: str = "Panel admina"
    admin_panel_link_role: str = "link"
    admin_panel_url_suffix: str = "/admin-panel/"

    # Service management
    service_heading_selector: str = "h3"
    slots_url_suffix: str = "/admin-panel/slots/"
    slot_item_selector: str = ".slot-item, [data-testid='slot'], tr"

    # Arrow separator in reservation items
    arrow_separator: str = "→"

    # Login form
    username_input_selector: str = "input[name='username']"
    password_input_selector: str = "input[type='password']"
    login_button_text: str = "Zaloguj"

    # Navigation links
    dashboard_link: str = "Dashboard"
    slots_link: str = "Terminy"
    add_service_link: str = "Dodaj usługę"
    add_slot_link: str = "+ Dodaj termin"
    save_button_text: str = "Zapisz"

    # Service form selectors
    service_name_input: str = "#id_name"
    service_description_input: str = "#id_description"
    service_price_input: str = "#id_price"
    service_duration_input: str = "#id_slot_duration"

    # Slot form selectors
    slot_service_select: str = "#id_service_select"
    slot_date_input: str = "#id_slot_date"
    slot_time_select: str = "#id_slots_select"


ADMIN_PANEL = AdminPanelData()
