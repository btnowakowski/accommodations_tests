def test_homepage_loads(page):
    page.goto("/")  # używa base_url z contextu

    # Title check
    assert "Booking" in page.title()

    # Navigation bar links
    page.get_by_role("link", name="Usługi").wait_for()
    page.get_by_role("link", name="Zaloguj").wait_for()
    page.get_by_role("link", name="Rejestracja").wait_for()

    # Main header / hero section
    hero = page.get_by_role(
        "heading", name="Wybierz usługę. Zarezerwuj termin. Gotowe."
    )
    assert hero.is_visible()
