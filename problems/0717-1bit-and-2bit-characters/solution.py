class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # iterate over the first n-2 bits
        i = 0
        while i < len(bits) - 2:
            # check if 2 bit char is ok
            two_bits = bits[i:i+2]
            if two_bits == [1, 1] or two_bits == [1, 0] or two_bits == [0, 0]:
                i += 2
                continue

            one_bit = bits[i]
            if one_bit == 0:
                i += 1
                continue

        # check last ones
        last_bits = bits[i:i+2]
        return last_bits == [0] or last_bits == [0, 0]
