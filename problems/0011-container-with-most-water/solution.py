class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Brute force O(n^2)"""
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            dist = right - left
            max_area = max(max_area, min(height[left], height[right]) * dist)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

