from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """sort and check for duplicit neighbors"""
        nums_sorted = sorted(nums)

        for i in range(len(nums) - 1):
            if nums_sorted[i] == nums_sorted[i + 1]:
                return True

        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        """check length of set vs length of nums"""
        return len(set(nums)) != len(nums)

    def containsDuplicate3(self, nums: List[int]) -> bool:
        """Using a set for visited elements"""
        visited = set()

        for i in nums:
            if i in visited:
                return True

            visited.add(i)

        return False
