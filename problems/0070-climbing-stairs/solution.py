class Solution:
    def climbStairs(self, n: int) -> int:
        """O(n) modified fibonacci"""
        res = 1
        prev = 0
        for i in range(1, n + 1):
            new = res + prev
            prev = res
            res = new
        return res
