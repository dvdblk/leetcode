class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        merged = ""
        while i < len(word1) and i < len(word2):
            merged += word1[i]
            merged += word2[i]

            i += 1
        
        if len(word1) > i:
            merged += word1[i:]
        elif len(word2) > i:
            merged += word2[i:]

        return merged
