# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        s = 0

        def dfs(node):
            nonlocal s
            if node is None:
                return node
            dfs(node.right)
            s += node.val
            node.val = s
            dfs(node.left)
            return node

        return dfs(root)
