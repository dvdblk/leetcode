class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        d = defaultdict(lambda: 0)

        for bill in bills:
            d[bill] += 1

            if bill == 10:
                if d[5] > 0:
                    d[5] -= 1
                else:
                    return False

            if bill == 20:
                if d[10] > 0 and d[5] > 0:
                    d[10] -= 1
                    d[5] -= 1
                elif d[5] > 2:
                    d[5] -= 3
                else:
                    return False

        return d[5] >= 0 and d[10] >= 0 and d[20] >= 0
