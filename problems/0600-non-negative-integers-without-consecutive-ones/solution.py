class Solution:
    def findIntegers(self, n: int) -> int:
        n_bit_length = len(bin(n)[2:])
        # memoize fibonacci using dp
        # (number of bit representations without consecutive ones per bit length)
        dp = [1, 2] + [0] * (n_bit_length-2)
        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]

        # only include the dp sums that have ones in them
        res = prev = 0
        for i in range(n_bit_length, -1, -1):
            # check if this bit is 1
            if n & (1 << i):
                res += dp[i]
                if prev:
                    # return sum if two consecutive ones appear
                    return res
                prev = 1
            else:
                prev = 0

        return res + 1