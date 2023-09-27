from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        for i in range(0, len(nums)):
            if nums[res] == val:
                nums.pop(res)
            else:
                res += 1

        return res
