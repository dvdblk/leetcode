from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        """Recursive DFS"""
        pre = []

        def dfs(node):
            nonlocal pre
            if node is not None:
                pre.append(node.val)
                for child in node.children:
                    dfs(child)

                return node

        dfs(root)
        return pre

    def preorder(self, root: "Node") -> List[int]:
        """Iterative DFS"""
        res = []
        stack = [root]

        while stack:
            node = stack.pop()

            if node is not None:
                res.append(node.val)
                for child in reversed(node.children):
                    stack.append(child)

        return res
