class Solution:
    def minimumLength(self, s: str) -> int:
        """two pointers"""
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                if left + 1 < len(s) and s[left + 1] == s[left] and left + 1 != right:
                    # move left ptr
                    left += 1
                elif right - 1 > 0 and s[right - 1] == s[right] and right - 1 != left:
                    # move right ptr
                    right -= 1
                else:
                    # clip suffix and prefix from s
                    s = s[left + 1 : right]
                    # reset left and right ptr
                    right = len(s) - 1
                    left = 0
            else:
                break

        return len(s)

    def minimumLength2(self, s: str) -> int:
        left = 0
        right = len(s) - 1
        min_length = len(s)

        while left < right:
            if s[left] == s[right]:
                if left + 1 < len(s) and s[left + 1] == s[left] and left + 1 != right:
                    left += 1
                elif right - 1 > 0 and s[right - 1] == s[right] and right - 1 != left:
                    right -= 1
                else:
                    min_length = min(min_length, right - left - 1)
                    left += 1
                    right -= 1
            else:
                break

        return min_length
