#!/usr/bin/python3
""" Module to determine the fewest number of coins needed to meet a given
amount."""


def makeChange(coins, total):
    """ Return fewest number of coins needed to meet total.
    """
    if not coins or coins is None:
        return -1

    if total <= 0:
        return 0

    num_coins_used = 0
    sorted_coins = sorted(coins)[::-1]

    for coin in sorted_coins:
        while coin <= total:
            total -= coin
            num_coins_used += 1
        if (total == 0):
            return num_coins_used
    return -1
