from typing import List
from heapq import heappush, heappop


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        h = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                x = arr[i] / arr[j]
                heappush(h, (x, [arr[i], arr[j]]))

        res = None
        for i in range(k):
            _, res = heappop(h)
        return res
