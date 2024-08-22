# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Difficulty: Medium
# Question: Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
#
# Example 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#
# Example 2:
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#
# Constraints:
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.
#

import collections
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Recursive solution
    Time complexity: O(n)
    Space complexity: O(n)
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Initialize the mapping of inorder values to their indices
        mapping = {}
        for i, elem in enumerate(inorder):
            mapping[elem] = i

        # Convert the preorder list to a deque (double ended queue) for efficient popping from the left. This is important because the preorder list is processed in a first-in-first-out manner.
        preorder = collections.deque(preorder)

        # Helper method to build the tree
        def build(start, end):
            # If the start index is greater than the end index, return None
            if start > end:
                return None

            # Pop the leftmost element from the preorder list and create a new TreeNode with the value
            root = TreeNode(preorder.popleft())

            # Find the index of the root value in the inorder list
            mid = mapping[root.val]

            # Recursively build the left and right subtrees
            root.left = build(start, mid - 1)
            root.right = build(mid + 1, end)

            return root

        return build(0, len(preorder) - 1)
