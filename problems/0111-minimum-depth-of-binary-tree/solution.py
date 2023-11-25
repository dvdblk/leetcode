from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            # Base case
            return 0
        elif root.left is not None and root.right is None:
            # Left subtree exists, Right doesn't
            return 1 + self.minDepth(root.left)
        elif root.left is None and root.right is not None:
            # Right subtree exists, Left doesn't
            return 1 + self.minDepth(root.right)
        else:
            # Both subtrees are present (return the min depth)
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
