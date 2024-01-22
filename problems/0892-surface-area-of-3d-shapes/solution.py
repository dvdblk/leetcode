class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        surface_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue

                # check all 6 sides for each position in the grid
                # start by checking boundaries (e.g. i==0, j==0)
                # then check neighbors' size

                # west
                if j == 0:
                    surface_area += grid[i][j]
                elif grid[i][j-1] < grid[i][j]:
                    surface_area += grid[i][j] - grid[i][j-1]

                # east
                if j == len(grid[i]) - 1:
                    surface_area += grid[i][j]
                elif grid[i][j+1] < grid[i][j]:
                    surface_area += grid[i][j] - grid[i][j+1]

                # north
                if i == 0:
                    surface_area += grid[i][j]
                elif grid[i-1][j] < grid[i][j]:
                    surface_area += grid[i][j] - grid[i-1][j]

                # south
                if i == len(grid) - 1:
                    surface_area += grid[i][j]
                elif grid[i+1][j] < grid[i][j]:
                    surface_area += grid[i][j] - grid[i+1][j]

                # bottom (base) + top
                surface_area += 2

        return surface_area