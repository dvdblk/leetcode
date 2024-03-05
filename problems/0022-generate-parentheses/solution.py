from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """backtracking (dfs)"""
        stack = [("", n, 0)]
        res = []

        while stack:
            s, opens_left, closes_left = stack.pop()

            if opens_left > 0:
                stack.append((s + "(", opens_left - 1, closes_left + 1))
            if closes_left > 0:
                stack.append((s + ")", opens_left, closes_left - 1))

            if opens_left == 0 and closes_left == 0:
                res.append(s)

        return res

    def generateParenthesis2(self, n: int) -> List[str]:
        """backtracking (recursive)"""
        result = []

        def backtrack(s, opens, closes):
            if len(s) == 2 * n:
                result.append(s)
                return

            if opens < n:
                backtrack(s + "(", opens + 1, closes)

            if closes < opens:
                backtrack(s + ")", opens, closes + 1)

        backtrack("", 0, 0)
        return result

    def generateParenthesis3(self, n: int) -> List[str]:
        """DP"""
        dp = {}
        dp[1] = ["()"]
        for i in range(2, n + 1):
            new_parens = set()
            for prev in dp[i - 1]:
                for j in range(len(prev)):
                    s = prev[:j] + "()" + prev[j:]
                    new_parens.add(s)
            dp[i] = list(new_parens)

        return dp[n]
