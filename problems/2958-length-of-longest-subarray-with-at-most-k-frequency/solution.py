from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        """Two pointers / sliding window"""
        freqs = defaultdict(int)
        longest_subarray = 0
        left = right = 0

        while right < len(nums):
            freqs[nums[right]] += 1

            while freqs[nums[right]] > k and left <= right:
                freqs[nums[left]] -= 1
                left += 1

            right += 1
            longest_subarray = max(longest_subarray, right - left)

        return longest_subarray
