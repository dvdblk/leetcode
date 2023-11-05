from typing import List

class Solution:
    def searchInsert_rec(self, nums: List[int], target: int) -> int:
        """Recursion

        Time O(log n)
        """
        if nums == []:
            return 0
        elif len(nums) == 1:
            if nums[0] >= target:
                return 0
            elif nums[0] < target:
                return 1
        else:
            mid = len(nums) // 2
            if target >= nums[mid]:
                return mid + self.searchInsert(nums[mid:], target)
            else:
                return self.searchInsert(nums[:mid], target)


    def searchInsert(self, nums: List[int], target: int) -> int:
        """While loop

        Time O(log n)
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid

        return l
