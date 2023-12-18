class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(reversed(sorted(set(nums))))

        if len(nums) < 3:
            return nums[0]
        else:
            return nums[2]

    def thirdMax2(self, nums: List[int]) -> int:
        """O(n) with list of maximum numbers"""
        # init list of max numbers
        max_i = [-math.inf] * 3

        for i in nums:
            if i > max_i[0]:
                max_i = [i, max_i[0], max_i[1]]
            elif i > max_i[1] and i < max_i[0]:
                max_i = [max_i[0], i, max_i[1]]
            elif i > max_i[2] and i < max_i[1]:
                max_i = [max_i[0], max_i[1], i]

        if len(nums) > 2:
            return max_i[2] if max_i[2] != -math.inf else max_i[0]
        else:
            return max_i[0]


