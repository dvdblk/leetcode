from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """Backtracking"""

        def backtrack(start, path):
            # start: starting index in s
            if start == len(s):
                result.append(path)
                return
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if sub == sub[::-1]:
                    backtrack(end, path + [sub])

        result = []
        backtrack(0, [])
        return result
