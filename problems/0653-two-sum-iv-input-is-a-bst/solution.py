# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """inorder + set"""
        def inorder(node):
            if node is None:
                return []
            else:
                return inorder(node.left) + [node.val] + inorder(node.right)

        bst = inorder(root)
        valid_operands = set()
        for num in bst:
            if k - num in valid_operands:
                return True
            valid_operands.add(num)

        return False

    def findTarget2(self, root: Optional[TreeNode], k: int) -> bool:
        """inorder + binary search"""
        def inorder(node):
            if node is None:
                return []
            else:
                return inorder(node.left) + [node.val] + inorder(node.right)

        bst = inorder(root)
        l = 0
        r = len(bst) - 1

        while l < r:
            cur_sum = bst[l] + bst[r]
            if cur_sum == k:
                return True
            elif cur_sum < k:
                l += 1
            else:
                r -= 1

        return False