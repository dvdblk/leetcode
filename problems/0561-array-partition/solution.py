from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # maximized sum of min pairs can be achieved by summing the even elements of a sorted nums array
        # [1, 2, 3, 4] = min(1, 2) + min(3, 4) = 1 + 3
        # [1, 2, 2, 5, 6, 6] = min(1, 2) + min(2, 5) + min(6, 6) = 1 + 2 + 6
        # [0, 0, 1, 3, 6, 7] = min(0, 0) + min(1, 3) + min(6, 7) = 0 + 1 + 6
        nums = sorted(nums)
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]

        return result
