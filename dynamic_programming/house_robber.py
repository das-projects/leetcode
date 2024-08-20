# 198. House Robber
# Link: https://leetcode.com/problems/house-robber/
# Difficulty: Medium
# Description:
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

# Approach:
# 1. We will use dynamic programming to solve this problem.
# 2. We will create a dp array of size n+1 where n is the length of the nums array.
# 3. dp[i] will be the maximum amount of money that can be robbed from the first i houses.
# 4. We will initialize dp[0] as 0 and dp[1] as nums[0].
# 5. We will iterate through the nums array and update the dp array based on the maximum amount of money that can be robbed from the first i houses.
# 6. Finally, we will return dp[n] where n is the length of the nums array.

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Get the length of the nums array
        n = len(nums)
        # If the length of the nums array is 0, return 0
        if n == 0:
            return 0
        # If the length of the nums array is 1, return the first element
        if n == 1:
            return nums[0]
        # Create a dp array of size n+1
        dp = [0] * (n + 1)
        # Initialize dp[0] as 0 and dp[1] as nums[0]
        dp[1] = nums[0]
        # Iterate through the nums array and update the dp array based on the maximum amount of money that can be robbed from the first i houses
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        # Return dp[n] where n is the length of the nums array
        return dp[n]