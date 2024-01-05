class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        """XOR with alternating bit mask"""
        bin_len = len(bin(n)[2:])
        mask = 1
        for i in range(bin_len-1):
            mask = mask << 1 | (i % 2)

        return n ^ mask == 0

