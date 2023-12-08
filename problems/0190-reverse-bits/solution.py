class Solution:
    def reverseBits(self, n: int) -> int:
        # int to bin, remove '0b', pad 0 from left until length is 32
        s = list(bin(n)[2:].zfill(32))
        # Reverse the list, i.e. [::-1]
        for i in range(len(s) // 2):
            tmp = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = tmp

        return int("0b" + "".join(s), 2)

    def reverseBits2(self, n: int) -> int:
        # Oneliner
        return int(bin(n)[2:].zfill(32)[::-1], 2)

    def reverseBits(self, n: int) -> int:
        # Using bitwise operators
        res = 0
        # Fixed number of steps
        for i in range(32):
            res <<= 1
            # for unsigned: n % 2 = n&1
            res += n & 1
            n >>= 1

        return res
