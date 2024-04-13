from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """O(n*m) row by row"""
        if not matrix:
            return 0

        n_cols = len(matrix[0])
        max_area = 0
        left, right = [0] * n_cols, [n_cols] * n_cols
        height = [0] * n_cols

        for i in range(len(matrix)):
            curr_left, curr_right = 0, n_cols
            for j in range(n_cols):
                if matrix[i][j] == "1":
                    height[j] += 1
                    left[j] = max(left[j], curr_left)
                else:
                    height[j] = 0
                    left[j] = 0
                    curr_left = j + 1

            for j in range(n_cols - 1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], curr_right)
                else:
                    right[j] = n_cols
                    curr_right = j

            for j in range(n_cols):
                max_area = max(max_area, height[j] * (right[j] - left[j]))

        return max_area
