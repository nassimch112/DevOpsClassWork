import pytest

from registration.src.registration import (
    collect_registration,
    is_valid_display_name,
    is_valid_email,
    is_valid_username,
)


@pytest.mark.parametrize("username", ["", "has space", "ADMIN", "root"])
def test_invalid_usernames(username):
    assert not is_valid_username(username)


def test_valid_username():
    assert is_valid_username("alice_42")


@pytest.mark.parametrize("email", ["alice.example.com", "alice@examplecom"])
def test_invalid_emails(email):
    assert not is_valid_email(email)


def test_valid_email():
    assert is_valid_email("alice@example.com")


@pytest.mark.parametrize(
    "display_name",
    ["ab", "a" * 21, "1alice", "alice-name", "Moderator"],
)
def test_invalid_display_names(display_name):
    assert not is_valid_display_name(display_name)


def test_valid_display_name():
    assert is_valid_display_name("Alice_42")


def test_registration_uses_username_when_display_name_is_empty(monkeypatch):
    values = iter(["alice", "alice@example.com", ""])
    monkeypatch.setattr("builtins.input", lambda _: next(values))

    assert collect_registration() == {
        "username": "alice",
        "email": "alice@example.com",
        "display_name": "alice",
    }


def test_registration_rejects_invalid_input(monkeypatch):
    values = iter(["root", "root@example.com", "root"])
    monkeypatch.setattr("builtins.input", lambda _: next(values))

    with pytest.raises(ValueError, match="Username"):
        collect_registration()
