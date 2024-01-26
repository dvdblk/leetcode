class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """Brute force O(n^3) gives TLE"""
        largest_perimeter = 0

        for a in range(len(nums)):
            for b in range(len(nums)):
                for c in range(len(nums)):
                    if a != b and b != c and a != c:
                        # check if triangle inequality holds
                        if nums[a] + nums[b] <= nums[c] or nums[a] + nums[c] <= nums[b] or nums[b] + nums[c] <= nums[a]:
                            continue

                        # compute perimeter
                        largest_perimeter = max(largest_perimeter, nums[a]+nums[b]+nums[c])

        return largest_perimeter

    def largestPerimeter2(self, nums: List[int]) -> int:
        """O(n log n)"""
        nums.sort()

        for i in range(len(nums)-1, 1, -1):
            a, b, c = nums[i], nums[i-1], nums[i-2]
            # check triangle ineq
            if a + b <= c or a + c <= b or c + b <= a:
                continue

            return a + b + c

        return 0