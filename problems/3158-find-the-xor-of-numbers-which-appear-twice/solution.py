from collections import Counter
from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = 0

        for k, v in c.items():
            if v == 2:
                res ^= k

        return res
