from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        low, high = newInterval
        res = []

        i = 0
        while i < len(intervals):
            l, r = intervals[i]

            if l <= low <= r or l <= high <= r or low <= l <= high or low <= r <= high:
                low, high = min(low, l), max(high, r)
            elif l > high:
                break
            else:
                res.append(intervals[i])

            i += 1

        res.append([low, high])
        for j in range(i, len(intervals)):
            res.append(intervals[j])

        return res
