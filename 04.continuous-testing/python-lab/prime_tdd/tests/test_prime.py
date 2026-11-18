import pytest

from prime_tdd.src.prime import is_prime


@pytest.mark.parametrize("number", [-5, 0, 1])
def test_numbers_less_than_two_are_not_prime(number):
    assert not is_prime(number)


def test_two_is_prime():
    assert is_prime(2)


@pytest.mark.parametrize("number", [4, 9, 25, 49])
def test_composite_numbers_are_not_prime(number):
    assert not is_prime(number)


@pytest.mark.parametrize("number", [3, 5, 17, 97])
def test_prime_numbers_are_prime(number):
    assert is_prime(number)
