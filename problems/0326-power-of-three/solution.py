class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n >= 3:
            return self.isPowerOfThree(n / 3)
        else:
            return False

    def isPowerOfThree2(self, n: int) -> bool:
        # check if the largest possible power of 3 is divisible by n
        return n > 0 and 3 ** 19 % n == 0