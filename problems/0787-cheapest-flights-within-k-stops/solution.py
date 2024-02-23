from collections import defaultdict, deque
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        """BFS"""
        outbound = defaultdict(list)

        for from_i, to_i, price_i in flights:
            outbound[from_i].append((to_i, price_i))

        visited = defaultdict(lambda: float("inf"))

        # node, current price, hops left (k)
        q = deque([(src, 0, k + 1)])

        while q:
            node, cur_price, hops_left = q.popleft()

            for out, p in outbound[node]:
                new_price = cur_price + p
                if hops_left - 1 >= 0 and new_price < visited[out]:
                    visited[out] = new_price
                    q.append((out, new_price, hops_left - 1))

        return visited[dst] if dst in visited else -1
