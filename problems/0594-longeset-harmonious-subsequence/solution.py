from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """O(n) w/ Counter hash map"""
        num_counter = Counter(nums)

        lhs = 0
        for k, v in num_counter.items():
            if v2 := num_counter.get(k - 1):
                lhs = max(lhs, v + v2)

        return lhs

    def findLHS_2(self, nums: List[int]) -> int:
        """O(n logn) sliding window after sort"""
        nums = sorted(nums)

        lhs = 0
        i = 0
        j = 1
        while j < len(nums):
            diff = nums[j] - nums[i]
            if diff == 1:
                # update lhs if diff is 1
                lhs = max(lhs, j - i + 1)
                # expand window
                j += 1
            elif diff == 0:
                # expand window
                j += 1
            else:
                # move window to the right if diff is large
                i += 1

        return lhs
