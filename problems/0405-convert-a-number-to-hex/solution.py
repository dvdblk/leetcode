class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        res = ""
        if num < 0:
            # use abs value
            num = (1 << 32) + num

        # hex digits
        f = {i: i for i in range(10)} | dict(zip(range(10, 16), "abcdef"))

        while num != 0:
            res += f"{f[num % 16]}"
            num = num // 16

        return res[::-1]