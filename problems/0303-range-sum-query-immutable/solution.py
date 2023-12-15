class NumArray:

    def __init__(self, nums: List[int]):
        sums = []

        acc = 0
        for i in nums:
            # accumulate sum
            acc += i
            sums.append(acc)
        self.sums = sums

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.sums[right] - self.sums[left-1]
        return self.sums[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)