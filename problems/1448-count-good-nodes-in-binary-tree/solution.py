# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, prev_val):
            if node is None:
                return 0
            else:
                if prev_val > node.val:
                    return 0 + dfs(node.left, prev_val) + dfs(node.right, prev_val)
                else:
                    return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)

        return dfs(root, -10e6)
