# 121. Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
# Question:
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
# Constraints:
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # If the prices list is empty, return 0
        if len(prices) == 0: 
            return 0

        # Initialize the profit to 0 and the minimum buy price to the first element in the prices
        profit = 0
        minBuy = prices[0] 
        # Iterate through the prices
        for i in range(len(prices)):
            profit = max(prices[i] - minBuy, profit)
            minBuy = min(minBuy, prices[i])
        return profit