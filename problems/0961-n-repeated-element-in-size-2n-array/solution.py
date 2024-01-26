class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[0][0]