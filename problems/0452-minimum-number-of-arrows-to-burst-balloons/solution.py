class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], x[1]))

        merged_points = []
        low, high = points[0]

        i = 0
        while i < len(points):
            l, r = points[i]
            if low <= l <= high or low <= r <= high or l <= low <= r or l <= high <= r:
                # merge multiple points into one point
                low, high = max(low, l), min(high, r)
            else:
                # append the intersecting previous points as one point
                merged_points.append([low, high])
                low, high = l, r
            i += 1

        merged_points.append([low, high])

        return len(merged_points)
