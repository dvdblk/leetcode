class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) <= k:
            return sum(nums)/len(nums)

        # sliding window sum of k elements (used to compute avg in the loop)
        running_sum = max_sum = sum(nums[:k])

        for i in range(1, len(nums)-k+1):
            running_sum -= nums[i-1]
            running_sum += nums[i+k-1]
            max_sum = max(max_sum, running_sum)

        return max_sum/k

