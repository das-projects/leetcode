# 98. Validate Binary Search Tree
# Link: https://leetcode.com/problems/validate-binary-search-tree/
# Difficulty: Medium
# Description:
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
# Input: root = [2,1,3]
# Output: true
# Example 2:
# Input: root = [5,1,4,null,null,3,6]
# Output: false

# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper Method:
        # DFS, Checking whether a tree is a valid BST
        def dfs_validBST(node, lower, upper):
            # If the node is None, return True
            if not node:
                return True

            # If the node's value is not within the range, return False
            if node.val <= lower or node.val >= upper:
                return False

            # Check whether the left and right subtrees are valid BST
            return dfs_validBST(node.left, lower, node.val) and dfs_validBST(node.right, node.val, upper)

        # Main Method:
        return dfs_validBST(root, float('-inf'), float('inf'))