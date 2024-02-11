from functools import cache
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """memoized DFS"""
        rows = len(grid)
        cols = len(grid[0]) - 1

        @cache
        def dfs(i, j1, j2):
            if i == rows - 1:
                # last row
                return grid[i][j1] + grid[i][j2] if j1 != j2 else grid[i][j1]
            else:
                cur = grid[i][j1] if j1 == j2 else grid[i][j1] + grid[i][j2]
                # can avoid this mess with nested forloop over [-1, 0, 1]
                return cur + max(
                    dfs(i + 1, max(j1 - 1, 0), j2),
                    dfs(i + 1, max(j1 - 1, 0), min(j2 + 1, cols)),
                    dfs(i + 1, max(j1 - 1, 0), max(j2 - 1, 0)),
                    dfs(i + 1, j1, j2),
                    dfs(i + 1, j1, min(j2 + 1, cols)),
                    dfs(i + 1, j1, max(j2 - 1, 0)),
                    dfs(i + 1, min(j1 + 1, cols), j2),
                    dfs(i + 1, min(j1 + 1, cols), min(j2 + 1, cols)),
                    dfs(i + 1, min(j1 + 1, cols), max(j2 - 1, 0)),
                )

        return dfs(0, 0, cols)
