"""Prime-number predicate used by the TDD exercise."""


def is_prime(number: int) -> bool:
    """Return whether number is a prime integer."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True
