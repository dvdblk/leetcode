from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, result = 1, nums[0]

        # Linear in time, constant in space
        for i in range(1, len(nums)):
            if nums[i] == result:
                # Bump count if same numbers
                count += 1
            else:
                if count == 0:
                    # Switch to new majority / result if count == 0
                    result = nums[i]
                    count += 1
                else:
                    count -= 1
        return result
