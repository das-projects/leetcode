# 102. Binary Tree Level Order Traversal
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Difficulty: Medium
# Description: Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
# Example 1:
# Input: [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Explanation:
# 3
# / \
# 9  20
#   /  \
# 15   7
# Example 2:
# Input: [1,2,3,4,null,null,5]
# Output: [[1],[2,3],[4,5]]
# Explanation:
# 1
# / \
# 2   3
# /     \
# 4       5
# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000


from typing import List, Optional
from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Using BFS to solve the problem
        self.d=defaultdict(list)
        # define the recursive function
        def foo(x, depth):
            # append the value of the node to the dictionary
            self.d[depth].append(x.val)
            # if the left or right child exists, call the function recursively
            if x.left: 
                foo(x.left,depth+1)
            if x.right: 
                foo(x.right,depth+1)
        # if the root exists, call the function
        if root: 
            foo(root,0)
        # return the values of the dictionary in sorted order of the keys
        return [self.d[i] for i in sorted(self.d.keys())]