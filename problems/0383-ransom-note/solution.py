class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """Hash table / dict"""
        # key = letter, value = nr of occurences of letter in magazine
        letters = {}

        # populate letters dict
        for ch in magazine:
            if letters.get(ch) is not None:
                letters[ch] += 1
            else:
                letters[ch] = 1

        # compare with ransomNote
        for ch in ransomNote:
            count = letters.get(ch)
            if count is None or count == 0:
                return False
            else:
                letters[ch] -= 1

        return True
