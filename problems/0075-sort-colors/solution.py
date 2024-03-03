from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # where to place the next 0
        zero_ptr = 0
        # where to place the next 2
        two_ptr = len(nums) - 1

        i = 0

        while i <= two_ptr:
            if nums[i] == 0:
                nums[zero_ptr], nums[i] = nums[i], nums[zero_ptr]
                zero_ptr += 1
                i += 1
            elif nums[i] == 2:
                nums[two_ptr], nums[i] = nums[i], nums[two_ptr]
                two_ptr -= 1
            else:
                i += 1

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # counting sort
        occurences = [0] * 3

        for num in nums:
            occurences[num] += 1

        res = [0] * occurences[0] + [1] * occurences[1] + [2] * occurences[2]
        for i in range(len(nums)):
            nums[i] = res[i]
