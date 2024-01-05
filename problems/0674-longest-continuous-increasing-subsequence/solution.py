class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_len = l = 1

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                l += 1
                max_len = max(max_len, l)
            else:
                l = 1

        return max_len