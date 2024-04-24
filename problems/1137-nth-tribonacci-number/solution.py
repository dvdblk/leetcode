from functools import cache


class Solution:
    def tribonacci(self, n: int) -> int:
        n += 1
        dp = [0] * max(n, 3)
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n - 1]

    @cache
    def tribonacci2(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return (
                self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
            )
