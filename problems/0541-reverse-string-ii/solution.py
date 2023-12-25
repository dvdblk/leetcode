class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """O(n) with slicing"""
        res = []
        i = 0
        while i < len(s):
            if i % (2 * k) == 0:
                # every 2k reverse the i+k substring
                # slicing below equiv to s[i:i+k][::-1]
                res.extend(s[i + k - 1 : i - 1 if i - 1 > 0 else None : -1])
                i += k
            else:
                # otherwise append s[i]
                res.append(s[i])
                i += 1

        return "".join(res)
