from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        _nums1 = nums1.copy()
        i, j = 0, 0
        for x in range(0, m + n):
            if j < n and i < m:
                if nums2[j] > _nums1[i]:
                    nums1[x] = _nums1[i]
                    i += 1
                else:
                    nums1[x] = nums2[j]
                    j += 1
            elif j < n:
                nums1[x] = nums2[j]
                j += 1
            elif i < m:
                nums1[x] = _nums1[i]
                i += 1
