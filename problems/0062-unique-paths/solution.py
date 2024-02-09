from functools import cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """bottom up DP (tabulation)"""
        dp = [[1] * n] * m
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    def uniquePaths2(self, m: int, n: int) -> int:
        """top down DP (memoization)"""

        @cache
        def dp(i, j):
            if i >= m or j >= n:
                # if we overshoot, stop recursion and return 0
                return 0
            elif i == m - 1 and j == n - 1:
                # base case, we reached the target
                return 1
            else:
                # sum up the paths to the right and down
                return dp(i + 1, j) + dp(i, j + 1)

        return dp(0, 0)
