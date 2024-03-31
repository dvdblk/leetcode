from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_idx = max_idx = tmp_idx = -1
        n_subarrays = 0

        for i in range(len(nums)):
            if nums[i] < minK or maxK < nums[i]:
                tmp_idx = i
            if minK == nums[i]:
                min_idx = i
            if maxK == nums[i]:
                max_idx = i

            n_subarrays += max(0, min(min_idx, max_idx) - tmp_idx)

        return n_subarrays
