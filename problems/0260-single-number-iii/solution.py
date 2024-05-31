from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        res = []
        for k, v in counter.items():
            if v == 1:
                res.append(k)

        return res
