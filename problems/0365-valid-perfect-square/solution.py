class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # linear search but exceeds time limit...
        if num == 1:
            return True

        for i in range(1, (num // 2) + 1):
            if i ** 2 == num:
                return True

        return False

    def isPerfectSquare2(self, num: int) -> bool:
        if num == 1:
            return True

        # binary search
        l, r = 0, num

        while l < r:
            mid = (l + r) // 2
            print(l, r, mid)
            res = mid ** 2
            if res == num:
                return True
            elif res < num:
                l = mid + 1
            else:
                r = mid

        return False
