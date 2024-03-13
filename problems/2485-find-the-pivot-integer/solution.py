class Solution:
    def pivotInteger(self, n: int) -> int:
        """Prefix sum hashmap solution. O(n) time, O(n) space."""
        prefix_sums = {}
        prefix_sum = 0

        for i in range(1, n + 1):
            prefix_sum += i
            prefix_sums[prefix_sum] = i

        prefix_sum = 0
        for i in range(n, 0, -1):
            prefix_sum += i

            if prefix_sum in prefix_sums and prefix_sums[prefix_sum] == i:
                return prefix_sums[prefix_sum]

        return -1
