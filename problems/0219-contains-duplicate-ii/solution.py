from typing import Optiopnal, List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """Use a dictionary to keep track of indices"""
        idx_dict = {}

        for i in range(len(nums)):
            j = idx_dict.get(nums[i])
            if j is not None and abs(i - j) <= k:
                return True
            else:
                idx_dict[nums[i]] = i
        return False
