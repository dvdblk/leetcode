class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        i = 0
        d = len(s)
        res = []
        for j in range(len(s)):
            if s[j] == "I":
                res.append(i)
                i += 1
            elif s[j] == "D":
                res.append(d)
                d -= 1
        res.append(d)
        return res