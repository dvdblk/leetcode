from typing import List

class Solution:
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        """Using a hashmap

        Time O(n), Space O(n)
        """
        addend_dict = {}

        for i in range(len(nums)):
            if addend_dict.get(target-nums[i]) is not None:
                return [addend_dict[target-nums[i]], i]
            addend_dict[nums[i]] = i

        return []

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        """Using two loops

        Time O(n^2), Space O(1)
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum_3(self, nums: List[int], target: int) -> List[int]:
        """Sort + one loop

        Time O(n log(n)), Space()
        """
        # Sort
        s_nums = sorted(nums)
        # Two pointers
        l, r = 0, len(nums)-1

        for i in range(1, len(nums)):
            val = s_nums[l] + s_nums[r]

            if val == target:
                # If we found the target, still need to locate the L + R indices
                l_idx = nums.index(s_nums[l])
                try:
                    # Avoid duplicit values
                    r_idx = nums.index(s_nums[r], l+1, len(nums))
                except ValueError:
                    # Otherwise search the entire list
                    r_idx = nums.index(s_nums[r])
                return [l_idx, r_idx]

            # If value is lower than target
            if val < target:
                # we are sure going to need a larger number so move right
                l += 1
            else:
                # otherwise move right pointer to the left to get a smaller number
                r -= 1




