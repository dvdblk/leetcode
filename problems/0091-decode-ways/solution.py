class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        dp = [1, 1]

        for i in range(2, len(s) + 1):
            one_digit = int(s[i - 1])
            two_digits = int(s[i - 2 : i])
            new = 0

            if one_digit != 0:
                new += dp[i - 1]

            if 10 <= two_digits <= 26:
                new += dp[i - 2]

            dp.append(new)

        return dp[len(s)]
