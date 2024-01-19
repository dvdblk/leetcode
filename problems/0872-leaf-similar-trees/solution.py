# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """O(n+m)"""
        def leaf_vals(node):
            if node is None:
                return []
            elif node.right is None and node.left is None:
                return [node.val]
            else:
                return leaf_vals(node.right) + leaf_vals(node.left)

        return leaf_vals(root1) == leaf_vals(root2)
