# 57. Insert Interval
# Link: https://leetcode.com/problems/insert-interval/
# Difficulty: Hard
# Description: Given a set of non-overlapping intervals where intervals[i] = [start_i, end_i] represent the start and the end of the ith interval and intervals is sorted in ascending order by the start of the interval. You are also given an interval newInterval = [start, end] that represents the start and end of another interval. 
# Insert newInterval into intervals such that intervals is still sorted in ascending order by the start of the interval. Additionally, the resulting set of intervals should be non-overlapping. Return the resulting set of intervals.
# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the newInterval [4,8] overlaps with [3,5],[6,7],[8,10].
# Constraints:
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= start_i <= end_i <= 10^5
# intervals is sorted by start_i in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 10^5

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        for interval in intervals:
			# the new interval is after the range of other interval, so we can leave the current interval baecause the new one does not overlap with it
            if interval[1] < newInterval[0]:
                result.append(interval)
            # the new interval's range is before the other, so we can add the new interval and update it to the current one
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            # the new interval is in the range of the other interval, we have an overlap, so we must choose the min for start and max for end of interval 
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        
        result.append(newInterval)
        return result