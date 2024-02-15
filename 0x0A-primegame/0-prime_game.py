#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of consecutive integers
starting from 1 up to and including n, they take turns choosing a prime
number from the set and removing that number and its multiples from the set.
The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally, determine
who the winner of each game is.

    Prototype: def isWinner(x, nums)
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    You cannot import any packages in this task

Example:

    x = 3, nums = [4, 5, 1]

First round: 4

    Maria picks 2 and removes 2, 4, leaving 1, 3
    Ben picks 3 and removes 3, leaving 1
    Ben wins because there are no prime numbers left for Maria to choose

Second round: 5

    Maria picks 2 and removes 2, 4, leaving 1, 3, 5
    Ben picks 3 and removes 3, leaving 1, 5
    Maria picks 5 and removes 5, leaving 1
    Maria wins because there are no prime numbers left for Ben to choose

Third round: 1

    Ben wins because there are no prime numbers for Maria to choose

Result: Ben has the most wins
"""


def isWinner(x, nums):
    """
    Returns the name of the player that won the most rounds
    If the winner cannot be determined, return None
    Args:
        - x : the number of rounds
        - nums: an array of n
    """
    if x == 0 or len(nums) == 0:
        return None
    ben = 0
    maria = 0
    i = 0

    while i < x:
        primes = generate_primes(nums[i])
        if len(primes) % 2 == 0:
            ben += 1
        else:
            maria += 1
        i += 1

    if ben > maria:
        return 'Ben'
    else:
        return 'Maria'


def generate_primes(n):
    """
    returns a list of prime numbers between 1 and n
    """
    primes = []
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes
