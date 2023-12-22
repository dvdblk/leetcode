from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # counter for consecutive ones
        c = 0
        max_ones = 0

        for i in nums:
            if i == 1:
                c += 1
                if c > max_ones:
                    max_ones = c
            else:
                c = 0

        return max_ones
