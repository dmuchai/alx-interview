#!/usr/bin/python3
"""
Module: Game of choosing Prime numbers
"""


def sieve_primes(n):
    """Returns list of prime counts up to n using the Sieve of Eratosthenes"""
    is_prime = [False, False] + [True] * (n - 1)  # index 0 and 1 are not prime
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    prime_count = [0] * (n + 1)
    count = 0
    for i in range(n + 1):
        if is_prime[i]:
            count += 1
        prime_count[i] = count
    return prime_count


def isWinner(x, nums):
    """
    Determines the winner of Prime Game
    Args:
        x (int): number of rounds
        nums (list): list of integers for each round
    Returns:
        str or None: Name of the winner or None if there's a tie
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    prime_counts = sieve_primes(max_num)

    maria_wins = 0
    for n in nums:
        if prime_counts[n] % 2 != 0:
            maria_wins += 1

    if maria_wins * 2 > x:
        return "Maria"
    elif maria_wins * 2 < x:
        return "Ben"
    return None
