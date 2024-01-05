class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        d = Counter(nums)
        duplicated = 0
        total = n*(n+1)//2
        for k, v in d.items():
            if v == 2:
                duplicated = k
            total -= k

        return [duplicated, total]