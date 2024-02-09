from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """dp starting from the top"""
        n = len(cost)
        dp = [0] * (n + 1)
        dp[n - 1] = cost[-1]
        for i in range(n - 2, -1, -1):
            dp[i] = min(cost[i] + dp[i + 1], cost[i] + dp[i + 2])

        return min(dp[0], dp[1])

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 2)

        for i in reversed(range(len(cost))):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])

        return min(dp[0], dp[1])
