from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return len(list(set(candyType))[: len(candyType) // 2])

    def distributeCandies2(self, candyType: List[int]) -> int:
        """O(n)"""
        candies = set()
        max_candies = len(candyType) // 2

        for i in range(len(candyType)):
            if candyType[i] in candies:
                continue
            else:
                candies.add(candyType[i])

            if len(candies) >= max_candies:
                break

        return len(candies)
