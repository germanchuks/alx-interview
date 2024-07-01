#!/usr/bin/python3
""" Determines the winner of a game based on rounds and numbers.
"""


def sieve_of_eratosthenes(n):
    """ Finds all primes less than or equal to n.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i, is_prime in enumerate(primes) if is_prime]


def isWinner(x, nums):
    """ Returns the name of the winner ("Ben" or "Maria") or None if it's a
    tie."""

    if x <= 0 or nums is None:
        return None

    max_value = max(nums)
    primes = sieve_of_eratosthenes(max_value)

    ben_score = 0
    maria_score = 0

    prefix_sums = [0] * (max_value + 1)
    for num in nums:
        prefix_sums[num] ^= 1

    for prime in primes:
        if prime > max_value:
            break

        divisor_count = (max_value // prime) + 1

        if prefix_sums[prime - 1] % 2 == 0:
            ben_score += divisor_count // 2
            maria_score += (divisor_count + 1) // 2
        else:
            maria_score += divisor_count // 2
            ben_score += (divisor_count + 1) // 2

    if ben_score > maria_score:
        return "Ben"
    elif maria_score > ben_score:
        return "Maria"
    else:
        return None
