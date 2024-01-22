class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True

        for i in range(1, len(nums)):
            increasing = increasing and nums[i-1] <= nums[i]
            decreasing = decreasing and nums[i-1] >= nums[i]

            if not increasing and not decreasing:
                return False

        return increasing or decreasing