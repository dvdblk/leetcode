class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * (26 + 2 * k)

        for c in s:
            i = ord(c) - ord("a") + k
            dp[i] = max(dp[i - k : i + k + 1]) + 1

        return max(dp)
