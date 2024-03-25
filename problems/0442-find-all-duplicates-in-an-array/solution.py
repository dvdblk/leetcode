from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            num = abs(num)

            if nums[num - 1] < 0:
                res.append(num)
            else:
                nums[num - 1] *= -1

        return res
