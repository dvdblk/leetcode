from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """bottom up DP"""
        if len(nums) < 2:
            return max(nums)

        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]

    def rob2(self, nums: List[int]) -> int:
        """top down DP"""
        dp = [0] * (len(nums) + 2)

        for i in range(len(nums) - 1, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])

        return dp[0]
