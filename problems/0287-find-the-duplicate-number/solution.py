from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            num = abs(num)
            if nums[num - 1] < 0:
                return num
            else:
                nums[num - 1] *= -1
        return -1
