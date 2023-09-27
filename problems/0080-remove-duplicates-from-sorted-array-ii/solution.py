from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Return short lists
        if len(nums) < 3:
            return len(nums)

        # Keep track whether values are repeating or not
        repeating = False
        # Previous value index
        prev = 0

        for i in range(1, len(nums)):
            if not repeating:
                if nums[prev] == nums[i]:
                    # Set repeating flag
                    repeating = True
                prev += 1
                nums[prev] = nums[i]
            elif nums[prev] != nums[i]:
                prev += 1
                nums[prev] = nums[i]
                repeating = False

        if repeating:
            nums[prev] = nums[len(nums) - 1]

        return prev + 1
