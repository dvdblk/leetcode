# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: "Node") -> int:
        """Recursive DFS"""
        if root is None:
            return 0
        else:
            # max(0, 0, ...) avoids exceptions for cases when result of map has len < 2
            return 1 + max(0, 0, *list(map(self.maxDepth, root.children)))

    def maxDepth_bfs(self, root: "Node") -> int:
        """Iterative BFS"""
        max_depth = 0
        queue = [(root, 1)]

        while queue:
            node, depth = queue.pop(0)

            if node is None:
                continue

            max_depth = max(max_depth, depth)

            # add all children to queue
            for child in node.children:
                queue.append((child, depth + 1))

        return max_depth
