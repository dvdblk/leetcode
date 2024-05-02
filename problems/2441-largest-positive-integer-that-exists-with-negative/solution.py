from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        max_k = -1
        n = [0] * 2048

        for num in nums:
            if n[-num]:
                max_k = max(max_k, abs(num))
            n[num] = 1

        return max_k
