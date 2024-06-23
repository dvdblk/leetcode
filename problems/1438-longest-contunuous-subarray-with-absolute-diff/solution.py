from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        min_q, max_q = deque(), deque()

        for n in nums:
            while max_q and n > max_q[-1]:
                max_q.pop()
            while min_q and n < min_q[-1]:
                min_q.pop()
            max_q.append(n)
            min_q.append(n)

            if max_q[0] - min_q[0] > limit:
                if max_q[0] == nums[left]:
                    max_q.popleft()
                if min_q[0] == nums[left]:
                    min_q.popleft()
                left += 1

        return len(nums) - left
