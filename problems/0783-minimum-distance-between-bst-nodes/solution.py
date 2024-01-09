# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        """Recursive dfs"""
        def dfs(node, a, b):
            if node is None:
                return b - a
            else:
                return min(dfs(node.left, a, node.val), dfs(node.right, node.val, b))

        return dfs(root, -10e5, 10e5)

    def minDiffInBST2(self, root: Optional[TreeNode]) -> int:
        """iterative DFS"""
        stack = [(root, False)]
        min_diff = 10e5
        prev = None
        inorder = []

        while stack:
            elem, visited = stack.pop()
            if elem is None:
                continue

            if visited:
                inorder.append(elem.val)
                if prev:
                    min_diff = min(min_diff, prev.val-elem.val)
                prev = elem
            else:
                stack.append((elem.left, False))
                stack.append((elem, True))
                stack.append((elem.right, False))

        return min_diff