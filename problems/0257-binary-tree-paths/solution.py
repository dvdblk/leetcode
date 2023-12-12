from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """DFS with recursion."""
        if root is None:
            return None
        paths = []

        def dfs(node, path):
            if node.left is None and node.right is None:
                # Leaf node
                paths.append(path)

            if node.left is not None:
                dfs(node.left, path + f"->{node.left.val}")
            if node.right is not None:
                dfs(node.right, path + f"->{node.right.val}")

        dfs(root, str(root.val))
        return paths
