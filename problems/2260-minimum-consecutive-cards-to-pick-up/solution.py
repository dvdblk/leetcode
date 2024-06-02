from collections import defaultdict
from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        positions = defaultdict(list)
        for i in range(len(cards)):
            positions[cards[i]].append(i)

        min_dist = len(cards) + 1
        for k, v in positions.items():

            for iv in range(1, len(v)):
                min_dist = min(min_dist, v[iv] - v[iv - 1])

        return -1 if min_dist == len(cards) + 1 else min_dist + 1
