from collections import defaultdict
from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        """DFS with path set to avoid cycles."""
        g = defaultdict(list)
        for s, d in edges:
            g[s].append(d)
            g[d].append(s)

        stack = [(d, set([source])) for d in g[source]]

        while stack:
            node, path = stack.pop()

            if node == destination:
                return True
            else:
                path.add(node)

                for d in g[node]:
                    if d not in path:
                        stack.append((d, path))

        return source == destination

    def validPath2(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        """(optimized) DFS via list of visited nodes"""
        g = defaultdict(list)
        for s, d in edges:
            g[s].append(d)
            g[d].append(s)

        visited = [0] * n
        stack = [source]

        while stack:
            node = stack.pop()

            if visited[node]:
                continue

            visited[node] = True
            for d in g[node]:
                stack.append(d)

        return visited[destination]
