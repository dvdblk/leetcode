from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        # Cyclic rotation: space O(1), time O(n)
        if len(nums) < 2:
            return
        if k >= len(nums):
            k = k % len(nums)
        if k == 0:
            return

        # Current index (pointer / position)
        ptr = 0
        # Index for tracking factors of k
        i = 0
        # Previous value
        prev = nums[-k % len(nums)]
        for _ in range(0, len(nums)):
            # Compute the idx to replace
            idx = (ptr + i * k) % len(nums)
            # Swap the value at idx with previous
            _tmp = nums[idx]
            nums[idx] = prev
            prev = _tmp

            i += 1
            # If the cycle is complete (next idx == ptr)
            if ptr == (ptr + i * k) % len(nums):
                # Bump ptr by one and attempt to finish the next cycle (if it exists)
                i = 0
                ptr += 1
                prev = nums[(ptr - k) % len(nums)]
