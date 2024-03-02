from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        max_len = 0
        n_zeros = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                n_zeros += 1

            while n_zeros > 1:
                if nums[left] == 0:
                    n_zeros -= 1
                left += 1

            max_len = max(max_len, right - left + 1 - n_zeros)

        return max_len - 1 if max_len == len(nums) else max_len
