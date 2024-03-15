from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minl = len(nums) + 1
        s = 0
        left = 0
        for r in range(len(nums)):
            s += nums[r]

            while left <= r and s >= target:
                minl = min(minl, r - left + 1)
                s -= nums[left]
                left += 1

        return minl if minl <= len(nums) else 0
