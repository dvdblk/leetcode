class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        """O(n) two passes"""
        max_elem_index = 0
        for i in range(len(nums)):
            if nums[i] > nums[max_elem_index]:
                max_elem_index = i

        for i in range(len(nums)):
            if i != max_elem_index and nums[max_elem_index] < nums[i]*2:
                return -1

        return max_elem_index

    def dominantIndex2(self, nums: List[int]) -> int:
        """O(n) one pass"""
        max_idx_1, max_idx_2 = 0, -1

        for i in range(1, len(nums)):
            if nums[i] > nums[max_idx_1]:
                max_idx_2 = max_idx_1
                max_idx_1 = i
            elif nums[i] > nums[max_idx_2]:
                max_idx_2 = i

        return max_idx_1 if nums[max_idx_1] >= nums[max_idx_2] * 2 else -1
