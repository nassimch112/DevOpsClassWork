"""Validation and command-line input helpers for user registration."""

import re
from collections.abc import Callable


BANNED_WORDS = frozenset({"admin", "mod", "moderator", "null", "root"})
_HANDLE_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9_]{2,19}$")


def is_valid_username(username: str) -> bool:
    """Return whether a username is non-empty, spaceless, and allowed."""
    normalized = username.strip().lower()
    return bool(normalized) and " " not in username and normalized not in BANNED_WORDS


def is_valid_email(email: str) -> bool:
    """Return whether an email contains the two basic required delimiters."""
    return "@" in email and "." in email


def is_valid_display_name(display_name: str) -> bool:
    """Return whether a display name follows the handle constraints."""
    return bool(_HANDLE_PATTERN.fullmatch(display_name)) and (
        display_name.lower() not in BANNED_WORDS
    )


def collect_registration(
    input_fn: Callable[[str], str] | None = None,
) -> dict[str, str]:
    """Read and validate registration fields from a command-line input function."""
    if input_fn is None:
        input_fn = input

    username = input_fn("Username: ")
    email = input_fn("Email: ")
    display_name = input_fn("Display name (optional): ")

    if not is_valid_username(username):
        raise ValueError("Username must be non-empty, spaceless, and not reserved.")
    if not is_valid_email(email):
        raise ValueError("Email must contain '@' and '.'.")

    display_name = display_name or username
    if not is_valid_display_name(display_name):
        raise ValueError(
            "Display name must be 3-20 characters, start with a letter, "
            "contain only letters, numbers, or underscores, and not be reserved."
        )

    return {
        "username": username,
        "email": email,
        "display_name": display_name,
    }


def main() -> None:
    registration = collect_registration()
    print(f"Registration accepted for {registration['username']}.")


if __name__ == "__main__":
    main()
