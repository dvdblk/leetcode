class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """Binary tree solution - O(log n)"""
        if n == 1:
            return 0

        n_symbols = 2 ** (n - 1)

        if k > (n_symbols // 2):
            return int(not self.kthGrammar(n, k - (n_symbols // 2)))
        else:
            return self.kthGrammar(n - 1, k)

    def kthGrammar2(self, n: int, k: int) -> int:
        """naive recursive solution - TLE"""

        def helper(s, n):
            if n == 0:
                return s
            else:
                new_s = ""
                for ch in s:
                    if ch == "0":
                        new_s += "01"
                    elif ch == "1":
                        new_s += "10"
                return helper(new_s, n - 1)

        result = helper("0", n)
        return int(result[k - 1])

    def kthGrammar3(self, n: int, k: int) -> int:
        """naive stack solution - TLE"""
        s = "01"

        i = 1
        while i < n:
            flipped = "".join(["0" if ch == "1" else "1" for ch in s])
            s += flipped
            i += 1

        return int(s[k - 1])
