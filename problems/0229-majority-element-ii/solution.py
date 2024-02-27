from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidates = defaultdict(lambda: 0)

        # keep count of top 2 elements
        for num in nums:
            candidates[num] += 1
            if len(candidates) > 2:
                # if there are more than 3 elements in the candidates,
                # decrement all counts by 1
                to_del = []
                for c in candidates.keys():
                    candidates[c] -= 1
                    if candidates[c] == 0:
                        to_del.append(c)

                # delete candidates that have a count of 0 to keep the candidates hashmap small
                for d in to_del:
                    del candidates[d]

        # count the total number of occurences of each candidate
        for k in candidates.keys():
            candidates[k] = 0
        for num in nums:
            if num in candidates:
                candidates[num] += 1

        # check if the candidates meet the condition
        res = []
        for k, v in candidates.items():
            if v > len(nums) // 3:
                res.append(k)
        return res
