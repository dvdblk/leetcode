from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # don't need k
        i = j = None

        for idx, num in enumerate(nums):
            if i is None or num <= nums[i]:
                i = idx
            elif j is None or num <= nums[j]:
                j = idx
            else:
                return True

        return False
