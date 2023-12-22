class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        # calculate the remainder that should be in the first group
        n_first_group = len(s) % k

        # result is a list of groups
        result = [s[:n_first_group]] if n_first_group > 0 else []
        s = s[n_first_group:]

        # add every k letters as a group
        for i in range(0, len(s), k):
            result.append(s[i : i + k])

        # join groups with a dash
        return "-".join(result)
