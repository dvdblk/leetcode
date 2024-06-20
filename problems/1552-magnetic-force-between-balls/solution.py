from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def can_place_balls(distance):
            prev, balls_left = 0, m
            for i in range(1, len(position)):
                if position[i] - position[prev] >= distance:
                    balls_left -= 1
                    prev = i
                    if balls_left == 1:
                        return True

            return False

        low, high = 1, position[-1] - position[0]
        result = 0
        while low <= high:
            mid = (low + high) // 2
            if can_place_balls(mid):
                result = max(result, mid)
                low = mid + 1
            else:
                high = mid - 1

        return result
