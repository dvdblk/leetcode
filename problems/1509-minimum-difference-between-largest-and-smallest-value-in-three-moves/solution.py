from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()

        min_diff = nums[-1] - nums[0]
        for i in range(4):
            if i < len(nums):
                diffs = [nums[-1 - i + j] - nums[0 + j] for j in range(i + 1)]
                min_diff = min(min_diff, *diffs)
        return min_diff
