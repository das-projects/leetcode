# 54. Spiral Matrix
# Link: https://leetcode.com/problems/spiral-matrix/
# Difficulty: Medium
# Description: Given an m x n matrix, return all elements of the matrix in spiral order.
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            # pop the first row each time
            result += matrix.pop(0)  
            # left rotate matrix 90 degree each time
            # zip(*matrix) is to transpose the matrix
            # [::-1] is to reverse the matrix
            matrix = list(zip(*matrix))[::-1]  
        return result