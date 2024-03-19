from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """Counter + sort (O(n log k))"""
        c = Counter(tasks)
        result = []

        n += 1
        while sum(c.values()) > 0:
            new = [-1 for _ in range(n)]
            i = 0

            for task_key, _ in c.most_common(n):
                remaining = c[task_key]
                if remaining > 0:
                    new[i] = task_key
                    c[task_key] -= 1
                    i += 1

            if sum(c.values()) == 0:
                result.extend(new[:i])
            else:
                result.extend(new)

        return len(result)

    def leastInterval2(self, tasks: List[str], n: int) -> int:
        """O(n)"""
        n += 1
        occurences = [0 for _ in range(26)]
        for task in tasks:
            occurences[ord(task) - ord("A")] += 1
        max_occ, n_max_occ = max(occurences), 0

        for occ in occurences:
            if occ == max_occ:
                n_max_occ += 1

        return max((max_occ - 1) * n + n_max_occ, len(tasks))
