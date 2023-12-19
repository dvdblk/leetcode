import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        """From quadratic equation"""
        return math.floor((-1 + math.sqrt(1 + 4 * 2 * n)) / 2)
