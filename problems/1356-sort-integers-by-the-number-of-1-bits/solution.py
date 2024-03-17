from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        h = []
        heapify(h)

        for n in arr:
            heappush(h, (n.bit_count(), n))

        result = []
        while h:
            result.append(heappop(h)[1])

        return result
