from typing import List
from heapq import heappop, heappush, heapify


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """min heap (smallest element stored at the root)"""
        k_largest = nums[:k]
        heapify(k_largest)

        for num in nums[k:]:
            if num > k_largest[0]:
                heappop(k_largest)
                heappush(k_largest, num)

        return k_largest[0]
