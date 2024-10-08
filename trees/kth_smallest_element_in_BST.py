# 230. Kth Smallest Element in a BST
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Difficulty: Medium
# Description:
# Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.
# Example 1:
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
# Constraints:
# The number of nodes in the tree is n.
# 1 <= k <= n <= 10^4
# 0 <= Node.val <= 10^4
# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Approach: Inorder Traversal to the kth value
        # Time Complexity: O(n)
        # Initialize the count and result
        self.count = 0
        self.result = 0

        # Helper Method:
        self.inorderTraversal(root, k)

        return self.result

    def inorderTraversal(self, node: Optional[TreeNode], k: int):
        # Base case
        if not node or self.count >= k:
            return

        # Recursively traverse the left subtree
        self.inorderTraversal(node.left, k)

        # Increment the count and check if the count is equal to k
        self.count += 1
        if self.count == k:
            self.result = node.val
            return

        # Recursively traverse the right subtree
        self.inorderTraversal(node.right, k)
