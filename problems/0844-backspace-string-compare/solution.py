class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_string(text):
            res = ""
            for ch in text:
                if ch == "#":
                    if len(res) > 0:
                        # basically popping from a stack here
                        res = res[:-1]
                else:
                    res += ch
            return res

        return get_string(s) == get_string(t)