from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        largest_altitude = 0
        prefix_sum = 0
        for i in range(len(gain)):
            prefix_sum += gain[i]
            largest_altitude = max(largest_altitude, prefix_sum)

        return largest_altitudea
