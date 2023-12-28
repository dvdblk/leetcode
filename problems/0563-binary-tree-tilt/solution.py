from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total_tilt = 0

        def dfs(node):
            nonlocal total_tilt
            if node is None:
                return 0
            else:
                sum_l = dfs(node.left)
                sum_r = dfs(node.right)
                total_tilt += abs(sum_l - sum_r)
                return node.val + sum_l + sum_r

        dfs(root)
        return total_tilt
