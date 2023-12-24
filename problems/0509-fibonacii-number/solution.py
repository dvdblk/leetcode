class Solution:
    def fib(self, n: int) -> int:
        """Recursive"""
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

    def fib(self, n: int) -> int:
        """DP"""
        fib_cache = [0, 1] + [0] * n
        for i in range(2, n + 1):
            fib_cache[i] = fib_cache[i - 1] + fib_cache[i - 2]
        return fib_cache[n]
