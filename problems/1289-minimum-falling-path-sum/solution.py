from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        """Recursively add the smallest two elements from the previous row to the current row."""

        def find_min(i):
            smolest, smol = 20000, 20001

            for j in range(len(grid[i])):
                if grid[i][j] < smolest:
                    smol = smolest
                    smolest = grid[i][j]
                elif grid[i][j] < smol:
                    smol = grid[i][j]
            return smolest, smol

        for row in range(1, len(grid)):
            smolest, smol = find_min(row - 1)
            for col in range(len(grid[row])):
                grid[row][col] += smolest if grid[row - 1][col] != smolest else smol

        return min(grid[-1])

    def minFallingPathSum2(self, grid: List[List[int]]) -> int:
        """DP"""
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        # init dp as the first grid row
        dp[0] = grid[0]

        for i in range(1, len(grid)):
            min1, min2 = 20000, 20001

            for j in range(len(dp[i - 1])):
                if dp[i - 1][j] < min1:
                    min2, min1 = min1, dp[i - 1][j]
                elif dp[i - 1][j] < min2:
                    min2 = dp[i - 1][j]

            for j in range(len(dp[i])):
                dp[i][j] = grid[i][j] + (min2 if dp[i - 1][j] == min1 else min1)

        return min(dp[-1])
