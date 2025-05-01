#!/usr/bin/python3
""" Minimum operations to reach n H characters """


def minOperations(n):
    """Returns the fewest number of operations to get n Hs"""
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
