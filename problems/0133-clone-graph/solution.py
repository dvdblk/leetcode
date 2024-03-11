# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, root: Optional["Node"]) -> Optional["Node"]:
        """initial dfs + hashmap solution"""
        d = dict()

        stack = [(root, None)]

        while stack:
            node, parent = stack.pop()

            if node is not None:
                if node.val in d:
                    ex = d[node.val]
                    if parent not in ex.neighbors:
                        ex.neighbors.append(parent)
                    continue

                new = Node(val=node.val)
                if parent:
                    parent.neighbors.append(new)
                    new.neighbors.append(parent)

                d[node.val] = new

                for neighbor in node.neighbors:
                    stack.append((neighbor, new))

        return d[root.val] if root is not None else None

    def cloneGraph2(self, root: Optional["Node"]) -> Optional["Node"]:
        """DFS + hashmap (no check for duplicate nodes)"""
        d = dict()
        stack = [root]

        while stack:
            node = stack.pop()

            if node is not None:
                # create new node if not in hashmap
                if node.val not in d:
                    new = Node(val=node.val)
                    d[node.val] = new

                # add undirected neighbors
                for neighbor in node.neighbors:
                    # create new neighbord node if not in hashmap
                    if neighbor.val not in d:
                        new_neighbor = Node(val=neighbor.val)
                        d[neighbor.val] = new_neighbor
                        stack.append(neighbor)
                    # add neighbor to the new node
                    d[node.val].neighbors.append(d[neighbor.val])

        return d[root.val] if root is not None else None

    def cloneGraph3(self, root: Optional["Node"]) -> Optional["Node"]:
        """recursive DFS + hashmap (no check for duplicate nodes)"""
        d = dict()

        def dfs(node):
            if node.val in d:
                return d[node.val]
            else:
                new = Node(val=node.val)
                d[node.val] = new

                for neighbor in node.neighbors:
                    new.neighbors.append(dfs(neighbor))

                return new

        return dfs(root) if root is not None else None
