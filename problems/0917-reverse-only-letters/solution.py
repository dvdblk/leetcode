class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            left_alpha = s[left].isalpha()
            right_alpha = s[right].isalpha()

            if left_alpha and right_alpha:
                # swap
                tmp = s[left]
                s[left] = s[right]
                s[right] = tmp
                # move
                left += 1
                right -= 1
            elif left_alpha:
                right -= 1
            elif right_alpha:
                left += 1
            else:
                left += 1
                right -= 1

        return "".join(s)