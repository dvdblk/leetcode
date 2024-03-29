from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """Sliding window"""
        max_elem = max(nums)
        freq = 0
        n_subarrays = 0
        left = right = 0

        while right < len(nums):
            freq += nums[right] == max_elem

            while freq >= k:
                freq -= nums[left] == max_elem
                left += 1

            right += 1
            n_subarrays += right - left

        return (len(nums) * (len(nums) + 1) // 2) - n_subarrays
