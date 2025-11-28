"""Test data module - centralized test data management."""

from tests.data.users import UserCredentials, generate_test_user
from tests.data.pages import HOMEPAGE, HomepageData
from tests.data.admin import ADMIN_PANEL, AdminPanelData
from tests.data.services import TEST_SERVICE, ServiceData
from tests.data.auth import AUTH_UI, AuthUIData
from tests.data.booking import BOOKING_UI, BookingUIData

__all__ = [
    "UserCredentials",
    "generate_test_user",
    "HOMEPAGE",
    "HomepageData",
    "ADMIN_PANEL",
    "AdminPanelData",
    "TEST_SERVICE",
    "ServiceData",
    "AUTH_UI",
    "AuthUIData",
    "BOOKING_UI",
    "BookingUIData",
]
