# 572. Subtree of Another Tree
# Link: https://leetcode.com/problems/subtree-of-another-tree/
# Difficulty: Easy
# Description:
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
# Example 1:
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
# Constraints:
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -10^4 <= root.val <= 10^4

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Helper Method:
        # DFS, Checking whether two trees are same
        def dfs_sameTree(node1, node2):
            # If both nodes are not None, check whether they are same tree
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                else:
                    return dfs_sameTree(node1.left, node2.left) and dfs_sameTree(node1.right, node2.right)
            elif not node1 and not node2:
                return True
            else:
                return False


        # Main Method:
        # Finding the matching root for the subRoot
        stack, rootNode = [root], None
        while stack:
            rootNode = stack.pop()
            if not rootNode: 
                continue

            # Once we have a match,  We check whether they are same tree.
            if rootNode.val == subRoot.val and dfs_sameTree(rootNode, subRoot): 
                return True
                
            stack.append(rootNode.right)
            stack.append(rootNode.left)

        return False