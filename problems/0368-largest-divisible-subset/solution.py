from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """DP - worst case O(n^2)

        Note: dp[i] contains the largest subset of elements that divide each other *including nums[i]*
        """
        nums.sort()

        dp = [[]] * len(nums)
        largest_subset = []

        for i in range(len(nums) - 1, -1, -1):
            candidate_subset = []
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    if len(dp[j]) > len(candidate_subset):
                        candidate_subset = dp[j]
            dp[i] = [nums[i]] + candidate_subset
            largest_subset = (
                dp[i] if len(largest_subset) < len(dp[i]) else largest_subset
            )

        return largest_subset
