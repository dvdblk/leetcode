class Solution:
    def mySqrt(self, x: int) -> int:
        """O(n) - naive / bruteforce solution"""
        if x < 2:
            return x

        for i in range(1, x):
            if i * i > x:
                return i - 1

        return 1

    def mySqrt_2(self, x: int) -> int:
        """O(log n) - binary search"""
        if x < 2:
            return x

        # [0, ..., x]
        left, right = 0, x
        mid = 0

        # while [ ..., L, ..., R, ... ]
        while left < right:
            # compute mid point [L, ..., mid, ..., R]
            mid = (left + right) // 2

            mid_sqr = mid * mid
            if mid_sqr < x:
                # check if mid is the same value as in the previous halving
                if left == mid:
                    # if yes return it because we found the result
                    return mid
                # otherwise set the new left as current mid
                left = mid
            elif mid_sqr == x:
                # case for perfect squares
                return mid
            else:
                right = mid

        return mid
