from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len, count = 0, 0
        occurences = {0: -1}

        for i in range(len(nums)):

            if nums[i]:
                count += 1
            else:
                count -= 1

            if occurences.get(count) is None:
                occurences[count] = i
            else:
                max_len = max(max_len, i - occurences[count])

        return max_len
