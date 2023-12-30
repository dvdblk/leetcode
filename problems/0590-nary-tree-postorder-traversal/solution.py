from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        """Reverse preorder DFS"""
        res = []
        stack = [root]

        while stack:
            node = stack.pop()

            if node is not None:
                res.append(node.val)
                stack.extend(node.children)

        return res[::-1]

    def postorder2(self, root: "Node") -> List[int]:
        """iterative postorder DFS"""
        res = []
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if node is not None:
                if not visited:
                    stack.append((node, True))
                    stack.extend(map(lambda x: (x, False), reversed(node.children)))
                else:
                    res.append(node.val)

        return res
