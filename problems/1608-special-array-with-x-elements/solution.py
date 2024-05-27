from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        """O(n^2)"""
        nums.sort()

        for i in range(len(nums) + 1):
            count = 0

            for n in nums:
                if n >= i:
                    count += 1

            if count == i:
                return i

        return -1
