from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0, 0

            height_l, diameter_l = dfs(node.left)
            height_r, diameter_r = dfs(node.right)
            height = max(height_l, height_r) + 1
            diameter = max(diameter_l, diameter_r, height_l + height_r)

            return height, diameter

        _, diameter = dfs(root)
        return diameter
