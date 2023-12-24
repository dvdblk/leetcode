import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = [
            i + (num // i) for i in range(2, int(math.sqrt(num)) + 1) if num % i == 0
        ]
        return sum(divisors) + 1 == num if num > 1 else False
