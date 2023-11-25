from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, target):
            if node is None:
                # base case, return False if there is no node
                return False
            elif node.left is None and node.right is None:
                # leaf node, check if target equals value
                return target == node.val
            else:
                # every other node, check both subtrees and reduce target by node value
                return dfs(node.left, target - node.val) or dfs(node.right, target - node.val)

        # do this without dfs method but w/e
        return dfs(root, targetSum)