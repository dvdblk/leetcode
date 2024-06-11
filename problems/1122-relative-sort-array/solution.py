from collections import Counter
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)

        res = []
        for a in arr2:
            res.extend([a for _ in range(c[a])])
            c[a] = 0

        leftovers = []
        for a, freq in c.items():
            if freq > 0:
                leftovers.extend([a for _ in range(freq)])

        return res + sorted(leftovers)
