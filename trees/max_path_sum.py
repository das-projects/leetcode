# 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Difficulty: Hard
# Question: A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root. The path sum of a path is the sum of the node's values in the path. Given the root of a binary tree, return the maximum path sum of any path.
# A path is a path that starts from any node and ends at any node. It doesn't have to go through the root.
# Example 1:
# Input: root = [1,2,3]
# Output: 6
# Example 2:
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Constraints:
# The number of nodes in the tree is in the range [0, 3 * 10^4].
# -1000 <= Node.val <= 1000

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize the maximum path sum to negative infinity
        self.max_sum = float('-inf')
        
        def dfs(node):
            # If the node is None, return 0
            if not node:
                return 0
            # Recursively calculate the maximum path sum of the left and right subtrees
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            # Update the maximum path sum
            self.max_sum = max(self.max_sum, node.val + left + right)
            # Return the maximum path sum of the current node
            return node.val + max(left, right)
        
        # Start the depth-first search from the root node
        dfs(root)
        return self.max_sum