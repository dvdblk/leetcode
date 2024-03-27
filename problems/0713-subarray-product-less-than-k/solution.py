from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n_subarrays, product, l = 0, 1, 0

        for r in range(len(nums)):
            product *= nums[r]

            while product >= k and r >= l:
                product /= nums[l]
                l += 1

            n_subarrays += r - l + 1

        return n_subarrays
