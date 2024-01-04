class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """O(n log n)"""
        nums.sort()
        prod_1 = nums[0] * nums[1] * nums[-1]
        prod_2 = nums[-3] * nums[-2] * nums[-1]
        return prod_1 if prod_1 > prod_2 else prod_2

    def maximumProduct2(self, nums: List[int]) -> int:
        """O(n) time, O(n) space

        Note: tradeoff b/w time and space, keep the top3 largest and top2 smallest values
        """
        # init largest (top 3 max values) and smallest (top 2 min values)
        # -1000 <= nums[i] <= 1000
        largest = [-1000, -1000, -1000]
        smallest = [1000, 1000]

        for i in range(len(nums)):
            # update largest
            if nums[i] >= largest[0]:
                largest = [nums[i], largest[0], largest[1]]
            elif nums[i] >= largest[1]:
                largest = [largest[0], nums[i], largest[1]]
            elif nums[i] >= largest[2]:
                largest = [largest[0], largest[1], nums[i]]

            # update smallest
            if nums[i] <= smallest[0]:
                smallest = [nums[i], smallest[0]]
            elif nums[i] <= smallest[1]:
                smallest = [smallest[0], nums[i]]

        # return larger product
        prod_1 = largest[0] * largest[1] * largest[2]
        prod_2 = largest[0] * smallest[0] * smallest[1]
        return prod_1 if prod_1 >= prod_2 else prod_2