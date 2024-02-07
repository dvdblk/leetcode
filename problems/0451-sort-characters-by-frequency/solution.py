class Solution:
    def frequencySort(self, s: str) -> str:
        counted = Counter(s)
        res = ""
        for ch, n in counted.most_common():
            res += ch * n
        return res
