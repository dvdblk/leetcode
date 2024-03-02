from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        """O(nlogn) time | O(1) space with sorts and in-place negation"""
        nums.sort()

        has_zero = False

        # turn as many numbers into positive while k > 0
        for i in range(len(nums)):
            if nums[i] < 0:
                if k > 0:
                    nums[i] = -1 * nums[i]
                    k -= 1
            if nums[i] == 0:
                has_zero = True

        nums.sort()

        # if k is still positive and nums contains no zero,
        # negate the smallest number if needed
        if k > 0 and not has_zero:
            if k % 2 == 1:
                nums[0] *= -1

        return sum(nums)

    def largestSumAfterKNegations2(self, nums: List[int], k: int) -> int:
        """Heap"""
        negative = []
        heapify(negative)

        smallest = 101
        total = 0

        for _, n in enumerate(nums):
            if n < 0:
                heappush(negative, n)
            else:
                total += n

            smallest = min(smallest, abs(n))

        while negative and k > 0:
            total -= heappop(negative)
            k -= 1

        if negative:
            total += sum(negative)

        if k % 2:
            total -= 2 * smallest

        return total
