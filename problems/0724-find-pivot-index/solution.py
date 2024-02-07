from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for i, num in enumerate(nums):
            if left == right - num:
                return i
            left += num
            right -= num

        return -1

    def pivotIndex2(self, nums: List[int]) -> int:
        right_prefix_sum = [0] * (len(nums) + 1)

        for i in range(len(nums) - 1, -1, -1):
            right_prefix_sum[i] = right_prefix_sum[i + 1] + nums[i]

        left_prefix_sum = 0
        for i in range(len(nums)):
            if right_prefix_sum[i + 1] == left_prefix_sum:
                return i

            left_prefix_sum += nums[i]

        return -1

    def pivotIndex3(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_prefix_sum = 0

        for i in range(len(nums)):
            if left_prefix_sum == total_sum - nums[i] - left_prefix_sum:
                return i

            left_prefix_sum += nums[i]

        return -1
