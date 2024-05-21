from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        """Naive O(n*2^n)"""
        superset = [[]]
        for n in nums:
            superset += [sub + [n] for sub in superset]

        total_sum = 0
        for s in superset:
            subset_xor = 0
            for si in s:
                subset_xor ^= si

            total_sum += subset_xor
        return total_sum
