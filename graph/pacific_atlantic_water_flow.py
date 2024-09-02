# 417. Pacific Atlantic Water Flow
# Link: https://leetcode.com/problems/pacific-atlantic-water-flow/
# Difficulty: Medium
# Question: You are given an m x n integer matrix heights representing the height of each unit cell in a continent. The Pacific ocean touches the continent's left and top edges, and the Atlantic ocean touches the continent's right and bottom edges. Water can only flow in four directions: up, down, left, and right. Water flows from a cell to an adjacent one with an equal or lower height. Return a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.
# Example 1:
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Example 2:
# Input: heights = [[2,1],[1,2]]
# Output: [[0,0],[0,1],[1,0],[1,1]]
# Constraints:
# m == heights.length
# n == heights[i].length
# 1 <= m, n <= 200
# 0 <= heights[i][j] <= 10^5

from typing import List

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix),len(matrix[0])
        p_visited = set()
        a_visited = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def dfs(visited, x,y):
            visited.add((x,y))
            for dx, dy in directions:
                new_x, new_y = x+dx, y+dy
                if 0<=new_x<m and 0<=new_y<n and (new_x,new_y) not in visited and matrix[new_x][new_y]>=matrix[x][y]:
                    dfs(visited, new_x,new_y)
        #iterate from left border and right border
        for i in range(m):
            dfs(p_visited,i,0)
            dfs(a_visited,i,n-1)
        #iterate from up border and bottom border
        for j in range(n):
            dfs(p_visited,0,j)
            dfs(a_visited,m-1,j)
        #The intersections of two sets are coordinates where water can flow to both P and A
        return list(p_visited.intersection(a_visited))