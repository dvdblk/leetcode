from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        perimeter = 0
        for i in range(n):
            m = len(grid[i])
            for j in range(m):
                if grid[i][j] == 1:
                    # by default there are 4 walls per island square
                    n_walls = 4

                    # Check neighbors
                    if i != 0:
                        # check above
                        n_walls -= grid[i - 1][j]

                    if i + 1 < n:
                        # check below
                        n_walls -= grid[i + 1][j]

                    if j != 0:
                        # check left
                        n_walls -= grid[i][j - 1]

                    if j + 1 < m:
                        # check right
                        n_walls -= grid[i][j + 1]

                    perimeter += n_walls
        return perimeter

    def islandPerimeter2(self, grid: List[List[int]]) -> int:
        """Iterative DFS"""
        perimeter = 0
        visited = set()
        to_visit = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    to_visit.append((i, j))

                    # DFS
                    while to_visit:
                        e_i, e_j = to_visit.pop()

                        if (e_i, e_j) in visited:
                            continue

                        if (
                            e_i < 0
                            or e_j < 0
                            or e_i == len(grid)
                            or e_j == len(grid[e_i])
                            or grid[e_i][e_j] == 0
                        ):
                            perimeter += 1
                            continue

                        visited.add((e_i, e_j))
                        to_visit.extend(
                            [
                                (e_i + 1, e_j),
                                (e_i - 1, e_j),
                                (e_i, e_j + 1),
                                (e_i, e_j - 1),
                            ]
                        )

        return perimeter
