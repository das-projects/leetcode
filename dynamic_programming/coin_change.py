# 322. Coin Change
# Link: https://leetcode.com/problems/coin-change/
# Difficulty: Medium
# Description:
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.
# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
# Input: coins = [2], amount = 3
# Output: -1
# Example 3:
# Input: coins = [1], amount = 0
# Output: 0

# Constraints:
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Time complexity: O(n*amount) where n is the number of coins
        # Space complexity: O(amount)

        # Initialize the dp array with amount + 1
        dp = [amount + 1] * (amount + 1)
        # Base case where the fewest number of coins to make up 0 is 0
        dp[0] = 0
        
        # Iterate through the dp array
        for i in range(1, amount + 1):
            # Iterate through the coins
            for coin in coins:
                # Update the dp array with the fewest number of coins
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        # Return -1 if the amount cannot be made up by any combination of the coins
        return dp[amount] if dp[amount] != amount + 1 else -1