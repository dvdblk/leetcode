from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """O(n) loop over the list twice, can mark existing numbers by
        placing them outside of the 1 <= n <= 10^5 bounds. Here I use negative numbers
        """

        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result
