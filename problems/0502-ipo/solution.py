from heapq import heappush, heappop
from typing import List


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        projects = sorted(zip(capital, profits))

        max_heap = []
        i = 0

        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                heappush(max_heap, -projects[i][1])
                i += 1

            if not max_heap:
                break

            print(max_heap)
            w += -heappop(max_heap)

        return w
