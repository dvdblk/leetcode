from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def explore(i, j):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])) or grid[i][j] == 0:
                return 0
            cur_pos = grid[i][j]
            grid[i][j] = 0
            score = cur_pos
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                score = max(score, cur_pos + explore(i + dx, j + dy))

            grid[i][j] = cur_pos
            return score

        max_score = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    max_score = max(max_score, explore(i, j))

        return max_score
