from collections import Counter
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """O(N^2) time - compare each row with each column."""
        n_equal = 0

        rows, cols = [""] * len(grid), [""] * len(grid)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                cols[j] += str(grid[i][j]) + ","
                rows[i] += str(grid[i][j]) + ","

        for row in rows:
            for col in cols:
                if row == col:
                    n_equal += 1

        return n_equal

    def equalPairs(self, grid: List[List[int]]) -> int:
        n_equal = 0

        cols = Counter(zip(*grid))

        for row in grid:
            n_equal += cols[tuple(row)]

        return n_equal
