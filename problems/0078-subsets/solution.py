from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Iterative approach O(n*2^n)"""
        powerset = [[]]
        for n in nums:
            powerset += [[n] + e for e in powerset]

        return powerset

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        """Bitwise operations"""
        n = len(nums)
        result = []
        for i in range(2**n):
            subset = []
            for j in range(n):
                if i & (1 << j):
                    subset.append(nums[j])
            result.append(subset)
        return result
