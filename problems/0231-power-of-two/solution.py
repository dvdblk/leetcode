class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """Using number of 1 bits; O(1) time | O(1) space"""
        return n > 0 and n.bit_count() == 1

    def isPowerOfTwo_2(self, n: int) -> bool:
        """Using log2; O(1) time | O(1) space"""
        return n > 0 and math.log2(n).is_integer()