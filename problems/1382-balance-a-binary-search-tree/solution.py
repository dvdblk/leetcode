# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def inorder(node):
            if node is None:
                return []
            else:
                return inorder(node.left) + [node.val] + inorder(node.right)

        vals = inorder(root)

        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(vals[mid])
            root.left, root.right = build(l, mid - 1), build(mid + 1, r)
            return root

        return build(0, len(vals) - 1)
