from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """DFS with stack"""
        numbers_sum = 0

        stack = [("", root)]

        while stack:
            n, node = stack.pop()

            if node is None:
                continue

            new_n = n + str(node.val)
            if node.left is None and node.right is None:
                numbers_sum += int(new_n)
            else:
                stack.append((new_n, node.left))
                stack.append((new_n, node.right))

        return numbers_sum

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """DFS with recursion"""

        def dfs(n, node):
            if node is None:
                return 0
            else:
                new_n = n * 10 + node.val
                if node.left is None and node.right is None:
                    return new_n
                else:
                    return dfs(new_n, node.left) + dfs(new_n, node.right)

        return dfs(0, root)
