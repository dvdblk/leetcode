class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return (x ^ y).bit_count()

    def hammingDistance(self, x: int, y: int) -> int:
        """Manual bit counting"""
        result = 0
        xor = x ^ y
        while xor != 0:
            result += xor & 1
            xor >>= 1
        return result
