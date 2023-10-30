from typing import List

class Solution:
    def jump(self, nums: List[int]) -> bool:

        # Save the number of jumps required
        n_jumps = 0
        # left and right indices for a window of values where we land after 1 jump
        ptr_l, ptr_r = 0, 0

        # Until the right pointer is outside of the bounds of the list
        while ptr_r < len(nums) - 1:
            # Current maximum is the left pointer
            max_pos = ptr_l

            for i in range(ptr_l, ptr_r+1):
                # keep track of the longest jump from this jump window
                if i+nums[i] >= max_pos:
                    max_pos = i+nums[i]

            # Update next window
            # next L is right next to previous R
            ptr_l = ptr_r+1
            # next R is the longest jump
            ptr_r = max_pos
            # increment jumps
            n_jumps += 1

        return n_jumps

    def jump_dp(self, nums: List[int]) -> bool:
        """
        O(n^2) with dynamic programming
        """
        # store how many jumps it takes to reach each index
        n_jumps = [10e5] * len(nums)
        # first index takes 0 jumps
        n_jumps[0] = 0

        # for each index
        for i in range(len(nums)):
            # for all the indices up to index i
            for j in range(i):
                # if we can jump from j to i
                if j + nums[j] >= i:
                    # update n_jumps[i] if it is smaller than prev value
                    n_jumps[i] = min(n_jumps[i], n_jumps[j] + 1)

        return n_jumps[-1]