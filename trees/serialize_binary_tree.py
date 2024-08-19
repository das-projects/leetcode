# 297. Serialize and Deserialize Binary Tree
# Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Difficulty: Hard
# Description:
# Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
# Example 1:
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:
# Input: root = []
# Output: []
# Constraints:
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Using BFS to serialize the tree
        def helper(node):
            if not node:
                return "N,"
            return str(node.val) + "," + helper(node.left) + helper(node.right)

        return helper(root)
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        values = iter(data.split(","))
        
        def helper(values):
            val = next(values)
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = helper(values)
            node.right = helper(values)
            return node

        return helper(values)
    

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))