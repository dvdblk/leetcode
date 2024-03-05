from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """DFS"""
        n_islands = 0

        def check_land(i, j):
            grid[i][j] = "2"

            for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (
                    0 <= ii < len(grid)
                    and 0 <= jj < len(grid[0])
                    and grid[ii][jj] == "1"
                ):
                    check_land(ii, jj)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    check_land(i, j)
                    n_islands += 1

        return n_islands
