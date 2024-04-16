from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if root is None:
            return None
        elif depth == 1:
            new_root = TreeNode(val=val, left=root, right=None)
            return new_root
        elif depth == 2:
            left_node = TreeNode(val=val, left=root.left, right=None)
            right_node = TreeNode(val=val, left=None, right=root.right)
            root.left = left_node
            root.right = right_node
            return root
        elif depth > 2:
            root.left = self.addOneRow(root.left, val, depth - 1)
            root.right = self.addOneRow(root.right, val, depth - 1)
            return root
        else:
            return root
