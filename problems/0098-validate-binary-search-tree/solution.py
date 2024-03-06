from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, higher_than, lower_than):
            if node is None:
                return True
            else:
                if higher_than is not None and node.val <= higher_than:
                    return False
                if lower_than is not None and node.val >= lower_than:
                    return False

                left_maxval = (
                    node.val if lower_than is None else min(lower_than, node.val)
                )
                right_minval = (
                    node.val if higher_than is None else max(higher_than, node.val)
                )
                return dfs(node.left, higher_than, left_maxval) and dfs(
                    node.right, right_minval, lower_than
                )

        return dfs(root, None, None)
