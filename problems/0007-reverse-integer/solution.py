class Solution:
    def reverse(self, x: int) -> int:
        """Reverse a string repr of x and check for overfow"""
        is_negative = x < 0
        reversed_x = str(abs(x))[::-1]

        while reversed_x[0] == 0:
            reversed_x = reversed_x[1:]

        res = int(reversed_x)
        if is_negative:
            res *= -1
        if res < -(2**31) or res > 2**31 - 1:
            return 0
        return res
