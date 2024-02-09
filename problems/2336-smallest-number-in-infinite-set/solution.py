from heapq import heapify, heappop, heappush


class SmallestInfiniteSet:

    def __init__(self):
        numbers = [i for i in range(1, 1001)]
        self._duplicate_set = set(numbers)
        self.inf_set = numbers
        heapify(self.inf_set)

    def popSmallest(self) -> int:
        res = heappop(self.inf_set)
        self._duplicate_set.remove(res)
        return res

    def addBack(self, num: int) -> None:
        if num not in self._duplicate_set:
            heappush(self.inf_set, num)
            self._duplicate_set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
