from typing import List
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        s = sorted(deck)
        res = deque([])

        for i in reversed(s):
            if len(res) > 1:
                res.appendleft(res.pop())
            res.appendleft(i)

        return res
