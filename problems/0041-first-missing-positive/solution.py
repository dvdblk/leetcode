from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # O(n) cyclic sort and get the first index that contains an incorrect num
        i, n = 0, len(nums)

        while i < n:
            if 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                # swap
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        # find the first number that is not equal to i
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
