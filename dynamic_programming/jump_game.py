# 55. Jump Game
# Link: https://leetcode.com/problems/jump-game/
# Difficulty: Medium
# Description:
# Given an array of non-negative integers nums, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index.
# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
# Constraints:
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5

from typing import List

# Approach:
# 1. We will iterate through the array and keep track of the remaining gas.
# 2. If the remaining gas is less than 0, we will return False.
# 3. If the current element is greater than the remaining gas, we will update the remaining gas.
# 4. Otherwise, we will decrement the remaining gas by 1.
# 5. Finally, we will return True.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1
            
        return True