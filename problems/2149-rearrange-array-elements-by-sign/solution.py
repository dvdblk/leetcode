from collections import deque
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_queue = deque()
        neg_queue = deque()

        for num in nums:
            if num < 0:
                neg_queue.append(num)
            else:
                pos_queue.append(num)

        res = []
        while neg_queue:
            res.append(pos_queue.popleft())
            res.append(neg_queue.popleft())

        return res
