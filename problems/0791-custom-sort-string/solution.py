from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """O(n^2) solution with O(n) space"""
        pivot = 0
        res = list(s)
        for ordered_ch in order:
            for i in range(pivot, len(s)):
                if res[i] == ordered_ch:
                    res[i], res[pivot] = res[pivot], res[i]
                    pivot += 1

        return "".join(res)

    def customSortString(self, order: str, s: str) -> str:
        """O(n) solution with O(n) space"""
        c = Counter(s)
        res = ""

        for ch in order:
            res += ch * c[ch]

        for ch in c:
            if ch not in order:
                res += ch * c[ch]

        return res
