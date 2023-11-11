from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # traversal comparison
        stack = [(p, q)]

        while stack:
            fst, snd = stack.pop()

            if fst and snd and fst.val == snd.val:
                stack.append((fst.right, snd.right))
                stack.append((fst.left, snd.left))
            elif fst or snd:
                return False
        return True
