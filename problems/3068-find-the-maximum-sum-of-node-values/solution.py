from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        """O(n logn)"""
        # xored and 'normalized' nums
        xored_nums = [(n ^ k) - n for n in nums]
        xored_nums.sort(reverse=True)

        # starting point is the sum of all nodes
        res = sum(nums)

        # keep adding the biggest differences between consecutive node pairs
        for i in range(0, len(nums) - 1, 2):
            diff = xored_nums[i] + xored_nums[i + 1]
            if diff > 0:
                res += diff
            else:
                break

        return res
