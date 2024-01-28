class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return [nums[0]**2]

        result = deque()
        left = 0
        right = len(nums)-1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.appendleft(nums[left] ** 2)
                left += 1
            else:
                result.appendleft(nums[right] ** 2)
                right -= 1

        return result