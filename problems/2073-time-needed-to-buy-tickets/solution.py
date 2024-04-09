from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """Brute-force"""
        time = 0

        i = 0
        while tickets[k] > 0:
            if tickets[i] > 0:
                time += 1
                tickets[i] -= 1
            i += 1
            if i == len(tickets):
                i = 0

        return time

    def timeRequiredToBuy2(self, tickets: List[int], k: int) -> int:
        """O(n) one pass"""
        time = 0

        for i, t in enumerate(tickets):
            if i <= k:
                time += min(tickets[i], tickets[k])
            else:
                time += min(tickets[i], tickets[k] - 1)

        return time
