from collections import Counter
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """O(n*m) solution."""
        n_pairs = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % (nums2[j] * k) == 0:
                    n_pairs += 1
        return n_pairs

    def numberOfPairs2(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """O(n*m) solution with hashtable."""
        n_pairs = 0
        c = Counter(nums1)

        for j in range(len(nums2)):
            for n, freq in c.items():
                if n % (nums2[j] * k) == 0:
                    n_pairs += freq

        return n_pairs
