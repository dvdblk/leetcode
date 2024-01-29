class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        """Two lists"""
        number = 0
        for n in num:
            number = number*10 + n
        number += k

        res = []
        while number > 0:
            remainder = number % 10
            number //= 10
            res = [remainder] + res

        return res

    def addToArrayForm2(self, num: List[int], k: int) -> List[int]:
        """Add to num array directly with carry forward"""
        # carry the remainder forward
        for i in range(len(num)-1, -1, -1):
            num[i] += k
            k, r = divmod(num[i], 10)
            num[i] = r

        # check if remainder is empty
        while k > 0:
            k, r = divmod(k, 10)
            num = [r] + num
        return num

