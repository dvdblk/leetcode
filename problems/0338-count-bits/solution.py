class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(i.bit_count())

        return res

    def countBits2(self, n: int) -> List[int]:
        """Using bitwise operations"""
        res = []
        for i in range(n+1):
            b = i
            n = 0
            while b:
                n += b & 1
                b >>= 1
            res.append(n)

        return res