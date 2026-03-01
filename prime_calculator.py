import math

def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_up_to(limit: int) -> list:
    """
    Finds all prime numbers up to a given limit.

    Args:
        limit (int): The upper limit to find prime numbers.

    Returns:
        list: A list of prime numbers up to the given limit.
    """
    primes = []
    for num in range(2, limit):
        if is_prime(num):
            primes.append(num)
    return primes