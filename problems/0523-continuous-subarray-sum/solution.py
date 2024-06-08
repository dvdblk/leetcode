from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = 0
        remainders = {}
        for i in range(len(nums)):
            prefix_sum += nums[i]
            remainder = prefix_sum % k

            if i >= 1 and remainder == 0:
                return True

            if remainder in remainders:
                if i - remainders[remainder] >= 2:
                    return True
            else:
                remainders[remainder] = i

        return False
