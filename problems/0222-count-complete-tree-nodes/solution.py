from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """O(n) time with recursion"""
        if root is None:
            return 0
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countNodes_2(self, root: Optional[TreeNode]) -> int:
        """O(n) time iterative solution"""
        result = 0
        node_stack = [root]

        # iterate until there are no nodes left
        while node_stack:
            if node := node_stack.pop():
                result += 1

                node_stack.extend([node.left, node.right])

        return result

    def countNodes_3(self, root: Optional[TreeNode]) -> int:
        """less than O(n)"""
        # Get height of left subtree
        height_l = 0
        curr = root
        while curr is not None:
            height_l += 1
            curr = curr.left

        # Get height of right subtree
        height_r = 0
        curr = root
        while curr is not None:
            height_r += 1
            curr = curr.right

        if height_l == height_r:
            # can compute the amount of nodes directly as heights are matching
            return 2**height_r - 1
        else:
            # recursively count the rest of the nodes
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
