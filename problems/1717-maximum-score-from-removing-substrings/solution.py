class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        points = 0
        i = 0

        smol, large = ((x, "ab"), (y, "ba")) if x < y else ((y, "ba"), (x, "ab"))

        while i < len(s):
            if s[i : i + 2] == large[1]:
                s = s[:i] + s[i + 2 :]
                points += large[0]
                i = max(0, i - 1)
            else:
                i += 1

        i = 0
        while i < len(s):
            if s[i : i + 2] == large[1]:
                s = s[:i] + s[i + 2 :]
                points += large[0]
                i = max(0, i - 1)
            elif s[i : i + 2] == smol[1]:
                s = s[:i] + s[i + 2 :]
                points += smol[0]
                i = max(0, i - 1)
            else:
                i += 1

        return points
