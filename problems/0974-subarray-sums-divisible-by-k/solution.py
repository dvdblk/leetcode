from typing import List
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum, count = 0, 0
        n_subarrays = defaultdict(int)
        n_subarrays[0] = 1

        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            count += n_subarrays.get(prefix_sum, 0)

            n_subarrays[prefix_sum] += 1

        return count
