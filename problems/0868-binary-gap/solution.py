class Solution:
    def binaryGap(self, n: int) -> int:
        bin_len = len(bin(n)[2:])
        last_one_index = None
        max_dist = 0

        for i in range(bin_len):
            if n & 1 == 1:
                if last_one_index is not None:
                    max_dist = max(max_dist, i - last_one_index)

                last_one_index = i

            n >>= 1

        return max_dist