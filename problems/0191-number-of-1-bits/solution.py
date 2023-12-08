class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        for i in range(32):
            # for unsigned can use n&1 instead of n%2
            result += n & 1
            n >>= 1
        return result
