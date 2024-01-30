class Solution:
    def robotWithString(self, s: str) -> str:
        c_s = Counter(s)
        t = []
        p = ""
        smallest = "a"
        for ch in s:
            t += ch
            c_s[ch] -= 1
            # update smallest value
            while smallest < "z" and c_s[smallest] == 0:
                smallest = chr(ord(smallest) + 1)
            # print on paper
            while t and t[-1] <= smallest:
                p += t.pop()

        return p