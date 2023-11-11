from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Recursive"""
        if root is None:
            return []
        else:
            return (
                self.inorderTraversal(root.left)
                + [root.val]
                + self.inorderTraversal(root.right)
            )

    def inorderTraversal_2(self, root: Optional[TreeNode]) -> List[int]:
        """Iterative with stack"""
        # stack where values are (node: TreeNode, visited: bool)
        stack = [(root, False)]
        res = []

        while stack:
            # pop the top of the stack
            node, visited = stack.pop()

            # check if the node exists
            if node is None:
                continue

            # check if we visited it previously (if it's the correct time to add it to the result)
            if visited:
                res.append(node.val)
            else:
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))

        return res
