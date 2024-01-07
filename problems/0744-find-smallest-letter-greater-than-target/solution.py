class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """O(n) time"""
        target = ord(target)

        for ch in letters:
            if ord(ch) > target:
                return ch

        return letters[0]

    def nextGreatestLetter2(self, letters: List[str], target: str) -> str:
        """O(log(n)) time | binary search"""
        left = 0
        right = len(letters) - 1

        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            elif letters[mid] > target:
                right = mid - 1

        return letters[0] if left >= len(letters) else letters[left]
