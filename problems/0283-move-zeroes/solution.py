class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, pos = 0, 0

        while i < len(nums):
            if nums[pos] == 0:
                nums.pop(pos)
                nums.append(0)
            else:
                pos += 1
            i += 1
