class Solution:
    def tribonacci(self, n: int) -> int:
        n += 1
        dp = [0] * max(n, 3)
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n - 1]
