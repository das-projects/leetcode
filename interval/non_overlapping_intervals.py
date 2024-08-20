# 435. Non-overlapping Intervals
# Link: https://leetcode.com/problems/non-overlapping-intervals/
# Difficulty: Medium
# Description: Given an array of intervals where intervals[i] = [start_i, end_i], find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
# Example 1:
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# Example 2:
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# Example 3:
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
# Constraints:
# 1 <= intervals.length <= 2 * 10^4
# intervals[i].length == 2
# -5 * 10^4 <= start_i < end_i <= 5 * 10^4

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Time complexity: O(nlogn) where n is the number of intervals
        # Space complexity: O(1)

        # Sort the intervals by the end time
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)

        prev = 0
        count = 1
        # Count the number of non-overlapping intervals
        for i in range(1, n):
            if intervals[i][0] >= intervals[prev][1]:
                prev = i
                count += 1

        return n - count