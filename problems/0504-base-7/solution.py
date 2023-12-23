class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        is_negative = True if num < 0 else False
        num = abs(num)
        base_7 = ""
        while num > 0:
            rem = num % 7
            num //= 7
            base_7 = str(rem) + base_7

        if is_negative:
            base_7 = "-" + base_7
        return base_7
