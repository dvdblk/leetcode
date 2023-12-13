class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            new = 0

            while num > 0:
                new += num % 10
                num = num // 10

            num = new

        return num