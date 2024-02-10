"""Inspired by: https://ics.uci.edu/~eppstein/161/960229.html"""

from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """Simple recursive solution - TLE"""
        if text1 == "" or text2 == "":
            return 0
        elif text1[0] == text2[0]:
            return 1 + self.longestCommonSubsequence(text1[1:], text2[1:])
        else:
            return max(
                self.longestCommonSubsequence(text1[1:], text2),
                self.longestCommonSubsequence(text1, text2[1:]),
            )

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        """Recursive with memoization via decorator"""

        @cache
        def lcs(i, j):
            if text1[i:] == "" or text2[j:] == "":
                return 0
            elif text1[i] == text2[j]:
                return 1 + lcs(i + 1, j + 1)
            else:
                return max(lcs(i + 1, j), lcs(i, j + 1))

        return lcs(0, 0)

    def longestCommonSubsequence3(self, text1: str, text2: str) -> int:
        """Recursive with explicit memoization"""

        cache = [[-1 for _ in range(1001)] for _ in range(1001)]

        def lcs(i, j):
            if cache[i][j] != -1:
                return cache[i][j]

            if text1[i:] == "" or text2[j:] == "":
                cache[i][j] = 0
            elif text1[i] == text2[j]:
                cache[i][j] = 1 + lcs(i + 1, j + 1)
            else:
                cache[i][j] = max(lcs(i + 1, j), lcs(i, j + 1))

            return cache[i][j]

        return lcs(0, 0)

    def longestCommonSubsequence4(self, text1: str, text2: str) -> int:
        """bottom up DP (tabulation)"""

        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]
