import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """O(n^2) - TLE"""
        until = int(math.sqrt(c))

        for i in range(0, until + 1):
            for j in range(0, until + 1):
                if i**2 + j**2 == c:
                    return True
        return False

    def judgeSquareSum2(self, c: int) -> bool:
        """O(n^2) - two pointers"""
        until = int(math.sqrt(c))

        left, right = 0, until

        while left <= right:
            l, r = left**2, right**2
            if l + r == c:
                return True
            elif l + r < c:
                left += 1
            else:
                right -= 1

        return False
