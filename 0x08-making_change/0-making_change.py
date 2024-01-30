#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total.

    Prototype: def makeChange(coins, total)
    Return: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    coins is a list of the values of the coins in your possession
    The value of a coin will always be an integer greater than 0
    You can assume you have an infinite number of each denomination of
      coin in the list
    Your solution’s runtime will be evaluated in this task
"""


def makeChange(coins, total):
    """
    returns fewest number of coins required to make change
    Args:
    - coins: list of the values of the coins in your possession
    - total: target amount
    """
    if total <= 0:
        return 0
    if total in coins:
        return 1

    coins.sort()
    right = len(coins) - 1
    count = 0
    while right >= 0:
        if total >= coins[right]:
            total -= coins[right]
            count += 1
        else:
            right -= 1
    if total == 0:
        return count
    return -1
