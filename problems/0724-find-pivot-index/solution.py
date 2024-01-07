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
