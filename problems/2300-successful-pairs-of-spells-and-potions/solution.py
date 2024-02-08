from typing import List
import math


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        res = [0] * len(spells)
        for i, spell in enumerate(spells):
            cutoff = math.ceil(success / spell)

            if potions[0] > cutoff:
                # skip binary search because all the potion values are greater than cutoff
                res[i] = len(potions)
            elif potions[-1] < cutoff:
                # skip binary search because all the potion values are less than cutoff
                res[i] = 0
            else:
                # binary search for index > cutoff
                left = 0
                right = len(potions)
                while left <= right:
                    mid = (left + right) // 2
                    if potions[mid] * spell >= success:
                        right = mid - 1
                    else:
                        left = mid + 1

                res[i] = len(potions) - left

        return res
