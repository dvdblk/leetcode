from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """Brute force recursive solution"""
        if root is None:
            return 0
        else:
            # Check if left node exists
            if root.left:
                # Check if left node is leaf
                if root.left.left is None and root.left.right is None:
                    # If right node exists
                    if root.right:
                        return root.left.val + self.sumOfLeftLeaves(root.right)
                    else:
                        return root.left.val
                else:
                    return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
            else:
                return self.sumOfLeftLeaves(root.right)

    def sumOfLeftLeaves_2(self, root: Optional[TreeNode]) -> int:
        """Recursive solution"""
        if root is None:
            return 0

        if root.left and root.left.left is None and root.left.right is None:
            return root.left.val + self.sumOfLeftLeaves_2(root.right)
        else:
            return self.sumOfLeftLeaves_2(root.left) + self.sumOfLeftLeaves_2(root.right)
