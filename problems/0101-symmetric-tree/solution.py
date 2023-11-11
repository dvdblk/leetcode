from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Recursive"""

        def check_symmetry(fst, snd) -> bool:
            if fst and snd:
                return (
                    fst.val == snd.val
                    and check_symmetry(fst.left, snd.right)
                    and check_symmetry(fst.right, snd.left)
                )
            else:
                return fst is None and snd is None

        return check_symmetry(root.left, root.right)

    def isSymmetric_2(self, root: Optional[TreeNode]) -> bool:
        """Iterative"""
        stack = [(root.left, root.right)]

        while stack:
            fst, snd = stack.pop()

            if fst and snd:
                if fst.val != snd.val:
                    return False
                else:
                    stack.append((fst.left, snd.right))
                    stack.append((fst.right, snd.left))
            elif fst or snd:
                return False
        return True
