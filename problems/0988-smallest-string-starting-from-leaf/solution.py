from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        smallest = chr(ord("z") + 1)

        def dfs(node, path):
            to_char = lambda x: chr(ord("a") + x)
            nonlocal smallest

            if node is None:
                pass
            elif node.left is None and node.right is None:
                final_path = (path + to_char(node.val))[::-1]
                smallest = min(smallest, final_path)
            else:
                dfs(node.left, path + to_char(node.val))
                dfs(node.right, path + to_char(node.val))

        dfs(root, "")

        return smallest
