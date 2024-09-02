# 128. Longest Consecutive Sequence
# Link: https://leetcode.com/problems/longest-consecutive-sequence/
# Difficulty: Hard
# Question: Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Constraints:
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        table = {}
        maxval = 0
        for num in nums:
            x = table.get(num - 1, 0)
            y = table.get(num + 1, 0)
            val = x + y + 1
            table[num - x] = val
            table[num + y] = val
            maxval = max(maxval, val)
        return maxval
