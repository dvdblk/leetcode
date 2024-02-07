from collections import deque
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Using a queue and sliding window
        """
        longest = 0
        # sliding window of 1s
        left = right = 0
        # queue of zero indices to know where to move the left pointer,
        # also counts the remaining flips
        zero_indices = deque()

        while right < len(nums):
            if nums[right] == 1:
                # extend window to the right
                right += 1
            elif nums[right] == 0 and len(zero_indices) < k:
                zero_indices.append(right)
                right += 1
            else:
                left = zero_indices.popleft() + 1 if zero_indices else left + 1
                right = max(left, right)

            longest = max(longest, right - left)
        return longest

    def longestOnes2(self, nums: List[int], k: int) -> int:
        # two pointers / sliding window
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1

            if k < 0:
                k += nums[left] == 0
                left += 1

        return right - left + 1
