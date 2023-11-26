class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_nr = nums[0]

        for i in range(1, len(nums)):
            single_nr ^= nums[i]

        return single_nr