from collections import Counter
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """Brute force solution gives TLE. O(n^2) time, O(1) space."""
        n_subarrays = 0
        for window_size in range(1, len(nums) + 1):
            s = sum(nums[:window_size])
            for i in range(window_size, len(nums) + 1):
                if s == goal:
                    n_subarrays += 1

                if i < len(nums):
                    s -= nums[i - window_size]
                    s += nums[i]

        return n_subarrays

    def numSubarraysWithSum2(self, nums: List[int], goal: int) -> int:
        """prefix sum + hashmap, O(n) time, O(1) space"""
        prefix, res = 0, 0
        # counts the number of valid subarrays
        counter = Counter({0: 1})

        for num in nums:
            prefix += num
            res += counter[prefix - goal]
            counter[prefix] += 1

        return res

    def numSubarraysWithSum3(self, nums: List[int], goal: int) -> int:
        """leq to goal - leq to (goal-1)"""

        def n_subarrays_with_leq_sum(target):
            if target < 0:
                return 0

            n = 0
            left = 0
            total_sum = 0

            for right in range(len(nums)):
                total_sum += nums[right]

                while total_sum > target:
                    total_sum -= nums[left]
                    left += 1

                n += right - left + 1

            return n

        return n_subarrays_with_leq_sum(goal) - n_subarrays_with_leq_sum(goal - 1)
