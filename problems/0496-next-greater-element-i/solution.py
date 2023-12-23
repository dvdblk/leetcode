from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """O(n^2) brute force"""
        res = []
        for i in range(len(nums1)):
            looking_for_next_greatest = False
            next_greatest = -1
            for j in range(len(nums2)):
                if not looking_for_next_greatest and nums1[i] == nums2[j]:
                    looking_for_next_greatest = True

                if looking_for_next_greatest and nums1[i] < nums2[j]:
                    next_greatest = nums2[j]
                    break
            res.append(next_greatest)

        return res

    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """O(n+m) with stack and dict"""
        d = dict()
        stack = []
        # add each n in nums2 to a stack
        for n in nums2:
            while stack and n > stack[-1]:
                # if the n is greater than top of stack,
                # pop the elements and save the n as the next greatest
                elem = stack.pop()
                d[elem] = n
            stack.append(n)

        # construct the resulting list
        res = []
        for n in nums1:
            res.append(d.get(n, -1))

        return res
