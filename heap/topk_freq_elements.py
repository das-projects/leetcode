# 347. Top K Frequent Elements
# Link: https://leetcode.com/problems/top-k-frequent-elements/
# Difficulty: Medium
# Description:
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Example:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example:
# Input: nums = [1], k = 1
# Output: [1]
# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

from collections import Counter
from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element
        map = Counter(nums)
        # Create a heap with the k most frequent elements
        # -count is used to create a max heap
        heap = [(-count, value) for value, count in map.items()]
        # heapify converts the list into a heap in O(n) time and O(n) space
        heapq.heapify(heap)

        # Extract the k most frequent elements
        result = []
        for _ in range(k):
            element = heapq.heappop(heap)
            result.append(element[1])
        return result
