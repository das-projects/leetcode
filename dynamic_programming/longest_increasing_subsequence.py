# 300. Longest Increasing Subsequence
# Link: https://leetcode.com/problems/longest-increasing-subsequence/
# Difficulty: Medium
# Description:
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
# Constraints:
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Time complexity: O(nlogn) where n is the length of nums
        # Space complexity: O(n)
        # Initialize the tails array with
        # the length of the list of numbers
        tails = [0] * len(nums)
        result = 0
        # Iterate through the numbers
        for num in nums:
            # Use binary search to find the index
            left_index, right_index = 0, result
            # Update the tails array
            while left_index != right_index:
                middle_index = left_index + (right_index - left_index) // 2
                if tails[middle_index] < num:
                    left_index = middle_index + 1
                else:
                    right_index = middle_index
            result = max(result, left_index + 1)
            tails[left_index] = num
        return result