class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # sort the lists
        nums1.sort()
        nums2.sort()

        res = []

        # use two pointers
        l, r = 0, 0

        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                # move the left pointer
                l += 1
            elif nums2[r] < nums1[l]:
                # move the right pointer
                r += 1
            else:
                # add current value to result
                res.append(nums1[l])
                # move both pointers
                l += 1
                r += 1
        return res