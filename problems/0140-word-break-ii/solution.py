from collections import deque
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        q = deque([(s, "")])
        visited = set()
        res = []

        while q:
            remaining, out = q.popleft()

            if (remaining, out) in visited:
                continue
            visited.add((remaining, out))

            if len(remaining) == 0:
                res.append(out.lstrip())
            else:
                for w in wordDict:
                    if remaining[: len(w)] == w:
                        q.append((remaining[len(w) :], out + " " + w))

        return res
