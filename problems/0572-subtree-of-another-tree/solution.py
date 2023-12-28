from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """Convert to inorder repr and check if subroot is in root"""

        def inorder(node):
            if node is None:
                return ""
            else:
                return f"{node.val},{inorder(node.left)},{inorder(node.right)} "

        root_flat = inorder(root)
        subroot_flat = inorder(subRoot)
        return (
            f",{subroot_flat}" in root_flat
            or subroot_flat == root_flat[: len(subroot_flat)]
        )

    def isSubtree_2(
        self, root: Optional[TreeNode], subRoot: Optional[TreeNode]
    ) -> bool:
        """O(n*m)"""

        def dfs_compare(node, subnode):
            if node is None and subnode is None:
                return True
            elif node is not None and subnode is not None:
                return (
                    node.val == subnode.val
                    and dfs_compare(node.right, subnode.right)
                    and dfs_compare(node.left, subnode.left)
                )
            else:
                return False

        if subRoot is None:
            return True

        if root is None:
            return False

        return (
            dfs_compare(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
