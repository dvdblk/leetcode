from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        max_local = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        max_local[i][j] = max(
                            max_local[i][j], grid[i + 1 + di][j + 1 + dj]
                        )

        return max_local
