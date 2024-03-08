from collections import defaultdict
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        max_freq = 0

        for num in nums:
            counts[num] += 1
            max_freq = max(max_freq, counts[num])

        res = 0
        for v in counts.values():
            if v == max_freq:
                res += v

        return res
