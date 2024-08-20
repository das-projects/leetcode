# 377. Combination Sum IV
# Link: https://leetcode.com/problems/combination-sum-iv/
# Difficulty: Medium
# Description:
# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
# The answer is guaranteed to fit in a 32-bit integer.
# Example 1:
# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
# Example 2:
# Input: nums = [9], target = 3
# Output: 0
# Constraints:
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# All the elements of nums are unique.
# 1 <= target <= 1000

# Approach:
# 1. We will use dynamic programming to solve this problem.
# 2. We will create a dp array of size target+1 where dp[i] will be the number of possible combinations that add up to i.
# 3. We will initialize dp[0] as 1 as there is only one way to add up to 0.
# 4. We will iterate through the dp array and update the values based on the sum of the previous values.
# 5. Finally, we will return dp[target].

from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Create a dp array of size target+1
        dp = [0] * (target + 1)
        # Initialize dp[0] as 1
        dp[0] = 1
        # Iterate through the dp array and update the values based on the sum of the previous values
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        # Return dp[target]
        return dp[target]