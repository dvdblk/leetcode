class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        occ_s, occ_t = {}, {}
        for i, ch in enumerate(s):
            occ_s[ch] = i
        for i, ch in enumerate(t):
            occ_t[ch] = i

        res = 0
        for ch in s:
            res += abs(occ_s[ch] - occ_t[ch])

        return res
