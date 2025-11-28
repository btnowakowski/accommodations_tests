from dataclasses import dataclass


@dataclass(frozen=True)
class HomepageData:
    """
    Homepage expected content for smoke tests.

    Attributes:
        title_contains: Expected substring in page title
        nav_links: Navigation links that should be visible
        hero_heading: Main hero section heading text
    """

    title_contains: str = "Booking"
    nav_links: tuple[str, ...] = ("Usługi", "Zaloguj", "Rejestracja")
    hero_heading: str = "Wybierz usługę. Zarezerwuj termin. Gotowe."


HOMEPAGE = HomepageData()
