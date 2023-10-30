from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # Save longest jump
        longest_jump = -1

        for i in range(len(nums)):
            if nums[i] > longest_jump:
                # Update longest jump
                longest_jump = nums[i]

            # Move one step every iteration of loop
            longest_jump -= 1

            # If we have no place to jump to and it's not the end of the list
            if longest_jump == -1 and i != len(nums)-1:
                # Return False
                return False

        return True