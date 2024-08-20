# 62. Unique Paths
# Link: https://leetcode.com/problems/unique-paths/
# Difficulty: Medium
# Description:
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?
# Example 1:
# Input: m = 3, n = 7
# Output: 28
# Example 2:
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
# Constraints:
# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10^9.

# Approach:
# 1. We will use dynamic programming to solve this problem.
# 2. We will create a dp array of size m x n where dp[i][j] will be the number of unique paths to reach the cell (i, j).
# 3. We will initialize the first row and the first column of the dp array as 1 as there is only one way to reach the cells in the first row and the first column.
# 4. We will iterate through the dp array and update the values based on the number of unique paths to reach the current cell.
# 5. Finally, we will return dp[m-1][n-1].

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[-1][-1]