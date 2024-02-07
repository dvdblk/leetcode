from collections import deque


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        window = deque()
        n_vowels = 0
        max_vowels = 0
        for i in range(len(s)):
            is_vowel = int(s[i] in vowels)
            n_vowels += is_vowel
            if i < k:
                window.append(is_vowel)
            else:
                n_vowels -= window.popleft()
                window.append(is_vowel)

            max_vowels = max(max_vowels, n_vowels)
            if max_vowels == k:
                return k

        return max_vowels
