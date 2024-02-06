from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Prefix and suffix sum"""
        prefix_sum = 1
        suffix_sum = 1
        result = [0] * len(nums)
        for i, num in enumerate(nums):
            result[i] = prefix_sum
            prefix_sum *= num

        for i in range(len(nums)-1, -1, -1):
            result[i] *= suffix_sum
            suffix_sum *= nums[i]

        return result
