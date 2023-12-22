from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        """O(n) time by summing the distance/duration to the next time point"""
        total_duration = 0
        for i in range(len(timeSeries) - 1):
            total_duration += min(duration, timeSeries[i + 1] - timeSeries[i])
        total_duration += duration
        return total_duration
