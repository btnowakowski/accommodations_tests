import re
from playwright.sync_api import expect
from tests.data import HOMEPAGE
from tests.helpers import home


def test_homepage_loads(page):
    page.goto("/")

    # Title check
    expect(page).to_have_title(re.compile(HOMEPAGE.title_contains))

    # Navigation bar links
    for link in home.get_nav_links(page):
        expect(link).to_be_visible()

    # Main header / hero section
    expect(home.get_hero_heading(page)).to_be_visible()
