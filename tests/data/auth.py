from dataclasses import dataclass


@dataclass(frozen=True)
class AuthUIData:
    """
    Authentication UI elements and labels.

    Attributes:
        register_link: Registration link text
        register_link_role: Registration link element role
        login_link: Login link text
        login_link_role: Login link element role
        logout_button: Logout button text
        logout_button_role: Logout button element role
        register_button: Register form submit button text
        register_button_role: Register button element role
        login_button: Login form submit button text
        login_button_role: Login button element role
        my_bookings_link: My bookings link text (visible when logged in)
        my_bookings_link_role: My bookings link element role
        password_label: Password field label
        email_label: Email field label
        username_input_selector: CSS selector for username input field
        password1_input_selector: CSS selector for password1 input field
        password2_input_selector: CSS selector for password2 input field
    """

    # Links
    register_link: str = "Rejestracja"
    register_link_role: str = "link"
    login_link: str = "Zaloguj"
    login_link_role: str = "link"
    my_bookings_link: str = "Moje rezerwacje"
    my_bookings_link_role: str = "link"

    # Buttons
    logout_button: str = "Wyloguj"
    logout_button_role: str = "button"
    register_button: str = "Załóż konto"
    register_button_role: str = "button"
    login_button: str = "Zaloguj"
    login_button_role: str = "button"

    # Labels and selectors
    password_label: str = "Hasło"
    email_label: str = "Email"
    username_input_selector: str = "input[name='username']"
    password1_input_selector: str = "input[name='password1']"
    password2_input_selector: str = "input[name='password2']"


AUTH_UI = AuthUIData()
