class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """Set difference"""
        all_numbers = set(range(len(nums)+1))
        diff = all_numbers.difference(set(nums))

        return diff.pop()

    def missingNumber_2(self, nums: List[int]) -> int:
        """Sum difference"""
        all_sum = sum(range(len(nums) + 1))
        nums_sum = sum(nums)

        return all_sum - nums_sum


