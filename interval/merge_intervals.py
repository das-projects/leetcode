# 56. Merge Intervals
# Link: https://leetcode.com/problems/merge-intervals/
# Difficulty: Medium
# Description: Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# Constraints:
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= start_i <= end_i <= 10^4

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time complexity: O(nlogn) where n is the number of intervals
        # Space complexity: O(n) where n is the number of intervals

        # If there are no intervals, return an empty list
        if not intervals:
            return []
        
        # Sort the intervals by the start time
        intervals.sort(key=lambda x: x[0])
        
        # Initialize the result list with the first interval
        result = [intervals[0]]
        
        # Iterate through the intervals
        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            last_interval = result[-1]
            
            # If the current interval overlaps with the last interval, merge them
            if current_interval[0] <= last_interval[1]:
                # Update the end time of the last interval
                last_interval[1] = max(last_interval[1], current_interval[1])
            else:
                # Add the current interval to the result list
                result.append(current_interval)
        
        return result