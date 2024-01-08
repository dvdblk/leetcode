class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """dp starting from the top"""
        n = len(cost)
        dp = [0] * (n + 1)
        dp[n-1] = cost[-1]
        for i in range(n-2, -1, -1):
            dp[i] = min(cost[i] + dp[i+1], cost[i] + dp[i+2])

        return min(dp[0], dp[1])