# 295. Find Median from Data Stream
# Link: https://leetcode.com/problems/find-median-from-data-stream/
# Difficulty: Hard
# Description:
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.
# Example:
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]
# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
# Constraints:
# -10^5 <= num <= 10^5
# There will be at most 5*10^4 calls to addNum and findMedian.
# There will be at least 1 element in the data structure when findMedian is called.
# Follow up:
# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

import heapq

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # Initialize two heaps: small to store the smaller half as a max heap
        # and large to store the larger half as a min heap
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # If large heap is not empty and the number is greater than the smallest number in large heap,
        # push it to the large heap. Otherwise, push the negation of the number to the small heap.
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        # Balance the heaps by adjusting their sizes if necessary
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # If sizes of both heaps are equal, return the average of the maximum element in the small heap
        # and the minimum element in the large heap
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0
    
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()