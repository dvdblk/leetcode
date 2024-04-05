class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) < 2:
            return s

        i = 0
        s = list(s)

        while i < len(s) - 1:
            if s[i].lower() == s[i + 1].lower() and s[i] != s[i + 1]:
                s.pop(i)
                s.pop(i)
                i = max(0, i - 1)
            else:
                i += 1

        return "".join(s)
