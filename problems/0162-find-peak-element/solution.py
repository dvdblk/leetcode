from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if mid > 0 and nums[mid] < nums[mid - 1]:
                # if left of mid is larger, go left
                right = mid
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                # if right of mid is larger, go right
                left = mid + 1
            else:
                # return mid (peak) if both adjacent are smaller
                return mid

        return mid
