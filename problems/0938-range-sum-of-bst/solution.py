# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        else:
            val = root.val if root.val >= low and root.val <= high else 0
            return val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)