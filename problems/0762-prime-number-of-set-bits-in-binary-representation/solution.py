class Solution:

    def is_prime(self, n) -> bool:
        if n <= 3:
            return n > 1
        if n % 2 == 0 or n % 3 == 0:
            return False
        limit = isqrt(n)
        for i in range(5, limit+1, 6):
            if n % i == 0 or n % (i+2) == 0:
                return False
        return True

    def countPrimeSetBits(self, left: int, right: int) -> int:
        n_prime = 0
        for i in range(left, right+1):
            n_prime += self.is_prime(i.bit_count())

        return n_prime