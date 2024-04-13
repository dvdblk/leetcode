from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """Brute-force"""
        max_level = max(height)
        total_water = 0

        for level in range(1, max_level + 1):
            left, right = -1, -1
            for i in range(len(height)):
                if height[i] >= level:
                    right = i

                    if right > left + 1 and left != -1:
                        total_water += right - (left + 1)

                    left = right

        return total_water

    def trap(self, height: List[int]) -> int:
        """Two pointers"""
        total_water, max_heightl, max_heightr = 0, 0, 0

        for h in height:
            max_heightl = max(max_heightl, h)
            total_water += max_heightl - h

        for h in reversed(height):
            if h == max_heightl:
                break

            max_heightr = max(max_heightr, h)
            total_water -= max_heightl - max_heightr

        return total_water
