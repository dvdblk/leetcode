# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """binary search O(log n)"""

        l, r = 1, n

        while l < r:
            mid = (l+r) // 2

            if isBadVersion(mid):
                # go left
                r = mid
            else:
                # go right
                l = mid + 1

        return l