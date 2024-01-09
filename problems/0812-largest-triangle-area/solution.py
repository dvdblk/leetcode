class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        vertices = combinations(points, 3)

        max_area = -1
        for v1, v2, v3 in vertices:
            area = 0.5 * abs(v1[0] * (v2[1] - v3[1]) + v2[0] * (v3[1] - v1[1]) + v3[0] * (v1[1] - v2[1]))
            max_area = max(max_area, area)

        return max_area