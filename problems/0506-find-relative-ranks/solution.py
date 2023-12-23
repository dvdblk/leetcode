from typing import List
from heapq import heappush, heappop


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """O(n log n) time and O(n) space"""
        heap = []
        for i, val in enumerate(score):
            heappush(heap, (-val, i))

        placements = [0] * len(score)
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [
            str(i + 1) for i in range(3, len(score))
        ]
        i = 0
        while heap:
            # get position in the original list, don't need the score
            _, pos = heappop(heap)
            placements[pos] = ranks[i]
            i += 1

        return placements

    def findRelativeRanks2(self, score: List[int]) -> List[str]:
        """Dict solution"""
        sorted_scores = reversed(sorted(score))
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [
            str(i + 1) for i in range(3, len(score))
        ]
        d = dict(zip(sorted_scores, ranks))

        return [d.get(val) for val in score]
