class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        area_sum = 0
        max_in_cols = [0 for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # top projection
                area_sum += grid[i][j] > 0
                # side projection
                max_in_cols[j] = max(max_in_cols[j], grid[i][j])

            # front projection
            area_sum += max(grid[i])

        for val in max_in_cols:
            # add side projection area
            area_sum += val

        return area_sum
