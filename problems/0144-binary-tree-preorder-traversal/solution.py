from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Recursive"""
        if root is None:
            return []
        else:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def preorderTraversal_it(self, root: Optional[TreeNode]) -> List[int]:
        """Iterative"""
        stack = [root]
        result = []

        while stack:
            # Pop a node
            node = stack.pop()

            if node is None:
                continue

            result.append(node.val)
            stack.append(node.right)
            stack.append(node.left)

        return result