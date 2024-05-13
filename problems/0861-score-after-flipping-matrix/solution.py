from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n_cols = len(grid[0])

        # flip the rows first if first bit is 0
        for i, row in enumerate(grid):
            if row[0] == 0:
                grid[i] = [1 - x for x in row]

        # flip the columns if needed
        for col in range(n_cols):
            n_ones = 0
            for row in range(len(grid)):
                n_ones += grid[row][col]
            n_zeros = len(grid) - n_ones
            if n_ones < n_zeros:
                for row in range(len(grid)):
                    grid[row][col] = 1 - grid[row][col]

        # return score
        score = 0
        for row in grid:
            out = 0
            for bit in row:
                out = (out << 1) | bit
            score += out

        return score
