from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """DFS with min diff between values as the tree is already sorted"""

        def dfs(node, a, b):
            if node is None:
                return b - a
            else:
                return min(dfs(node.left, a, node.val), dfs(node.right, node.val, b))

        return dfs(root, -10e5, 10e5)
