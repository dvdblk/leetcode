from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        group_coordinates = []

        def dfs(i, j):
            if 0 <= i < len(land) and 0 <= j < len(land[i]) and land[i][j] == 1:
                land[i][j] = 2
                # move down and to the right
                r1, c1 = dfs(i + 1, j)
                r2, c2 = dfs(i, j + 1)
                # take the max coords in both directions (and current pos)
                r = max(i, r1, r2)
                c = max(j, c1, c2)
                return (r, c)
            else:
                return (0, 0)

        for i in range(len(land)):
            for j in range(len(land[i])):
                if land[i][j] == 1:
                    r, c = dfs(i, j)
                    group_coordinates.append((i, j, r, c))

        return group_coordinates
