import math


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        """Binary search for the sum of a geometric series O(log n)"""
        num = int(n)
        # compute maximum amount of digits the number in target base can have
        # Note: base 2 is the lowest base so it will be the max because higher bases cannot
        #   be longer
        max_digits = int(math.log2(num)) + 1
        for i in range(max_digits, 2, -1):
            # binary search
            l, r = 2, num
            while l <= r:
                mid = (l + r) // 2
                geo_sum = ((mid**i) - 1) // (mid - 1)

                if geo_sum < num:
                    l = mid + 1
                elif geo_sum > num:
                    r = mid - 1
                else:
                    return str(mid)
        # return highest base if no other suitable base is found
        return str(num - 1)
