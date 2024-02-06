from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # keep track of the zero index that should be swapped
        zero_index = None

        for i, num in enumerate(nums):
            if num == 0:
                if zero_index is None:
                    zero_index = i
                else:
                    zero_index = min(i, zero_index)
            elif zero_index is not None:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index = min(i, zero_index + 1)

    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # place non-zero at the start of the list
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j += 1

        # fill the rest with zeros
        for i in range(j, len(nums)):
            nums[i] = 0
