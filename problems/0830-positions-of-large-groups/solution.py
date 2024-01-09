class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        cur_start = 0
        result = []
        # add a numeric value that will never occur in s at the end to include the last letter group
        s += "0"

        for i in range(1, len(s)):
            if s[cur_start] != s[i]:
                if i  - cur_start >= 3:
                    result.append([cur_start, i-1])
                cur_start = i
        return result