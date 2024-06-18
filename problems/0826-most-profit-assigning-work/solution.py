from typing import List


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        work = sorted(zip(profit, difficulty), reverse=True)

        total_profit = 0
        i = 0
        for w in sorted(worker, reverse=True):
            p, d = work[i]
            while i < len(work) and d > w:
                i += 1
                if i >= len(work):
                    return total_profit
                p, d = work[i]

            if d <= w:
                total_profit += p

        return total_profit
