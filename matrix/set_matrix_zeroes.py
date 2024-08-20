# 73. Set Matrix Zeroes
# Link: https://leetcode.com/problems/set-matrix-zeroes/
# Difficulty: Medium
# Description:
# Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.
# Follow up:
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
# Example:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
# Constraints:
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31 - 1

from typing import List

class Solution1:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        # First pass: record the rows and columns that are to be zeroed
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Second pass: set the rows to zero
        for row in zero_rows:
            for j in range(cols):
                matrix[row][j] = 0

        # Third pass: set the columns to zero
        for col in zero_cols:
            for i in range(rows):
                matrix[i][col] = 0


# Time complexity: O(m * n) where m is the number of rows and n is the number of columns in the matrix
# Space complexity: O(m + n) where m is the number of rows and n is the number of columns in the matrix

# Approach 2: Using O(1) Space
# We can reduce the space complexity to O(1) by using the first row and first column to store the information about the zero rows and columns.
# We can use two boolean variables to keep track of whether the first row and first column should be zeroed.
# We iterate through the matrix and use the first row and first column to store the information about the zero rows and columns.
# We then iterate through the matrix again and update the cells to be zero if they are in a zero row or column.

class Solution2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        first_row_has_zero = False
        first_col_has_zero = False

        # iterate through matrix to mark the zero row and cols
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = matrix[0][col] = 0

        # iterate through matrix to update the cell to be zero if it's in a zero row or col
        for row in range(1, m):
            for col in range(1, n):
                matrix[row][col] = (
                    0
                    if matrix[0][col] == 0 or matrix[row][0] == 0
                    else matrix[row][col]
                )

        # update the first row and col if they're zero
        if first_row_has_zero:
            for col in range(n):
                matrix[0][col] = 0

        if first_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0


# Time complexity: O(m * n) where m is the number of rows and n is the number of columns in the matrix
# Space complexity: O(1) since we are using constant space
