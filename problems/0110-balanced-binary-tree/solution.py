from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """Naive O(n^2)"""
        # Check depth of each subtree on every node
        def bin_tree_depth(node):
            if node is None:
                return 0
            return 1 + max(bin_tree_depth(node.left), bin_tree_depth(node.right))
        if root is None:
            return True

        if abs(bin_tree_depth(root.left) - bin_tree_depth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            # Return False if the depths of subtrees are larger than 1
            return False

    def isBalanced_2(self, root: Optional[TreeNode]) -> bool:
        """O(n) - only visits each node once"""

        def subtree_balance_and_depth(node):
            """Returns is_balanced and height of the tree"""
            if node is None:
                # Base case
                # None := balanced, 0 height
                return True, 0
            else:
                # check left subtree first
                l_b, l_d = subtree_balance_and_depth(node.left)
                if not l_b:
                    # return immediately if left subtree is not balanced
                    return l_b, 0
                r_b, r_d = subtree_balance_and_depth(node.right)

                # Check for balance, diff between subtree height has to be <= 1
                balanced = r_b and abs(l_d - r_d) <= 1

                return balanced, 1 + max(l_d, r_d)

        return subtree_balance_and_depth(root)[0]
