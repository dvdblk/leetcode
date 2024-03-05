from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """O(log n)"""
        # find pivot with binary search
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        if left > 0:
            nums = nums[left:] + nums[:left]
        pivot = left

        # find target with binary search
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return (mid + pivot) % len(nums)
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return -1
