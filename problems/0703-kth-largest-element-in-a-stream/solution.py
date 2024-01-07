class KthLargest:
    """insertion sort on every insert (inefficient af lul)"""

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        inserted = False
        for i in range(len(self.nums)):
            if self.nums[i] >= val:
                self.nums.insert(i, val)
                inserted = True
                break

        if not inserted:
            self.nums.append(val)

        if len(self.nums) < self.k:
            return 0
        return self.nums[-self.k]


class KthLargest2:
    """heap"""

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums[:k]
        heapify(self.nums)
        for i in range(k, len(nums)):
            if nums[i] > self.nums[0]:
                heappushpop(self.nums, nums[i])


    def add(self, val: int) -> int:
        heappush(self.nums, val)
        if len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)