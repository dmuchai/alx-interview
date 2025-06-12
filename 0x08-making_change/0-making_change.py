#!/usr/bin/python3
"""
Minimum Coins Change
"""
def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize DP array with total+1 (impossible high value)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make total 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
