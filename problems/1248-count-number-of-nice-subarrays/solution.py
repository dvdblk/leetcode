from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def n_subarrays(k):
            n = 0
            total = 0
            start = 0
            q = deque([])
            for end in range(len(nums)):
                if nums[end] % 2 == 1:
                    total += nums[end] % 2
                    q.append(end)

                if total > k:
                    total = k
                    start = q.popleft() + 1

                n += end - start + 1
            return n

        return n_subarrays(k) - n_subarrays(k - 1)
