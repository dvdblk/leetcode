class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        for i in range(32):
            if left == right:
                return left << i
            else:
                left >>= 1
                right >>= 1
        return 0
