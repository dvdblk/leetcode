from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        else:
            # construct result string
            result = f"{root.val}"
            left = self.tree2str(root.left)
            right = self.tree2str(root.right)


            if left != "" or right != "":
                result += f"({left})"
            if right != "":
                result += f"({right})"
            return result