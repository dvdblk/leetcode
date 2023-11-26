from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Recursive"""
        if root is None:
            return []
        else:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


    def postorderTraversal_it(self, root: Optional[TreeNode]) -> List[int]:
        """Iterative"""
        stack = [root]
        result = []

        while stack:
            node = stack.pop()

            if node is None:
                continue

            result.append(node.val)
            stack.append(node.left)
            stack.append(node.right)

        # Return the reversed list as
        return result[::-1]