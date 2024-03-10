from collections import defaultdict
from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """O(n^2) brute force"""
        # find nodes
        nodes = set()

        for fr, to in edges:
            nodes.add(fr)
            nodes.add(to)

        for node in nodes:
            ok = True
            for fr, to in edges:
                if fr != node and to != node:
                    ok = False
                    break

            if ok:
                return node

        return -1

    def findCenter2(self, edges: List[List[int]]) -> int:
        """O(n)"""
        degree = defaultdict(int)

        for fr, to in edges:
            degree[fr] += 1
            degree[to] += 1

        n = len(degree.keys())

        for k, v in degree.items():
            if v == n - 1:
                return k

        return -1

    def findCenter2(self, edges: List[List[int]]) -> int:
        """O(n) one pass"""
        degree = defaultdict(int)
        max_node, max_degree = -1, 0
        for fr, to in edges:
            degree[fr] += 1
            degree[to] += 1

            if max_degree < degree[to]:
                max_degree = degree[to]
                max_node = to

            if max_degree < degree[fr]:
                max_degree = degree[fr]
                max_node = fr

        return max_node