from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)

        capacity.sort()

        for i, c in enumerate(reversed(capacity)):
            apples -= c
            if apples <= 0:
                return i + 1

        return len(capacity)
