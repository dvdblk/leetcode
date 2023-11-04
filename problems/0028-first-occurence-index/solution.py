
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Bruteforce O(n*m)"""
        if len(haystack) == len(needle):
            return 0 if needle == haystack else -1

        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] == needle[0]:
                tmp_needle_start = i
                for j in range(1, len(needle)):
                    if haystack[i+j] != needle[j]:
                        tmp_needle_start = -1
                        break
                if tmp_needle_start != -1:
                    return tmp_needle_start


        return -1
