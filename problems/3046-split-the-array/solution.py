from collections import Counter
from typing import List


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        c = Counter(nums)

        for _, freq in c.items():
            if freq > 2:
                return False

        return True
