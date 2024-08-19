# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/
# Difficulty: Easy
# Question: Given the root of a binary tree, invert the tree, and return its root.
# Example 1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:
# Input: root = [2,1,3]
# Output: [2,3,1]
# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # If the root is None, return None
        if not root:
            return None
        # Recursively invert the left and right subtrees
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        # Swap the left and right subtrees
        root.left = right
        root.right = left
        return root