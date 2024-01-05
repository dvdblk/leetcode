# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        """recursive DFS"""
        def dfs(node, min_1, min_2):
            if node is None:
                return min_1, min_2
            else:
                # update min values
                if node.val < min_1:
                    min_2 = min_1
                    min_1 = node.val
                elif node.val != min_1 and node.val <= min_2:
                    min_2 = node.val
                # L + R
                min_1, min_2 = dfs(node.left, min_1, min_2)
                return dfs(node.right, min_1, min_2)

        min_1, min_2 = dfs(root, root.val, float("inf"))
        return min_2 if min_2 != float("inf") else -1