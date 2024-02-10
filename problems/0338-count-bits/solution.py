from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            res.append(i.bit_count())

        return res

    def countBits2(self, n: int) -> List[int]:
        """Using bitwise operations"""
        res = []
        for i in range(n + 1):
            b = i
            n = 0
            while b:
                n += b & 1
                b >>= 1
            res.append(n)

        return res

    def countBits3(self, n: int) -> List[int]:
        """Bitwise ops"""
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
