from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """DFS for each node and compare heights (TLE)"""
        g = defaultdict(list)
        for s, d in edges:
            g[s].append(d)
            g[d].append(s)

        def dfs(node, visited):
            if node is None or node in visited:
                return 0
            else:
                visited.add(node)
                d = list(map(lambda x: dfs(x, visited), g[node]))
                return 1 + max(-1, 0, *d)

        heights = []
        for i in range(n):
            heights.append(dfs(i, set()))

        min_height = min(heights)
        labels = []
        for i, height in enumerate(heights):
            if height == min_height:
                labels.append(i)

        return labels

    def findMinHeightTrees2(self, n: int, edges: List[List[int]]) -> List[int]:
        """Remove leaf nodes iteratively until only 1 or 2 nodes left."""

        if not edges:
            return [x for x in range(n)]

        g = defaultdict(list)

        for s, d in edges:
            g[s].append(d)
            g[d].append(s)

        n_nodes = n
        leaf_nodes = [node for node in range(n_nodes) if len(g[node]) == 1]

        while n_nodes > 2:
            new_leafs = []

            for leaf in leaf_nodes:
                parent = g[leaf][0]
                g[parent] = list(filter(lambda x: x != leaf, g[parent]))

                if len(g[parent]) == 1:
                    new_leafs.append(parent)

            n_nodes -= len(leaf_nodes)
            leaf_nodes = new_leafs

        return leaf_nodes

    def findMinHeightTrees3(self, n: int, edges: List[List[int]]) -> List[int]:
        """Same as findMinHeightTrees2 but with sets instead of lists."""
        if not edges:
            return [x for x in range(n)]

        g = defaultdict(set)

        for s, d in edges:
            g[s].add(d)
            g[d].add(s)

        n_nodes = n
        leaf_nodes = [node for node in range(n_nodes) if len(g[node]) == 1]

        while n_nodes > 2:
            new_leafs = []

            for leaf in leaf_nodes:
                parent = g[leaf].pop()
                g[parent].remove(leaf)

                if len(g[parent]) == 1:
                    new_leafs.append(parent)

            n_nodes -= len(leaf_nodes)
            leaf_nodes = new_leafs

        return leaf_nodes
