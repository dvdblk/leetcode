class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        n -= 1
        return (time % n) + 1 if (time // n) % 2 == 0 else n - (time % n) + 1
