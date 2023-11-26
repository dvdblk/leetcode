class Solution:
    def findComplement(self, num: int) -> int:
        """via Bitwise operations"""
        # print(bin(num))
        # print(bin(~num))
        # print(bin(2 ** num.bit_length() - 1))
        # print(bin(~num & (2 ** num.bit_length() - 1)))

        return ~num & (2 ** num.bit_length() - 1)