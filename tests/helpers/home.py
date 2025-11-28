from playwright.sync_api import Page
from tests.data import HOMEPAGE


def get_nav_links(page: Page):
    """Get all navigation links."""
    return [page.get_by_role("link", name=name) for name in HOMEPAGE.nav_links]


def get_hero_heading(page: Page):
    """Get hero section heading."""
    return page.get_by_role("heading", name=HOMEPAGE.hero_heading)
