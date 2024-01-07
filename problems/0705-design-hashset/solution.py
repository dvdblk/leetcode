class MyHashSet:
    """space optimized version of using a list of size 10e6"""

    def __init__(self):
        # self.set = [0] * int(10e6)
        self.set = []

    def add(self, key: int) -> None:
        # increase the length of self.set if needed
        if key >= len(self.set):
            self.set += [0] * (key - len(self.set) + 1)
        self.set[key] = 1

    def remove(self, key: int) -> None:
        # check if self.set is long enough
        if key < len(self.set):
            self.set[key] = 0

    def contains(self, key: int) -> bool:
        # check if self.set is long enough
        if key >= len(self.set):
            return False
        return self.set[key]


class MyHashSet2:
    """bit manipulation"""

    def __init__(self):
        self.array = 0

    def add(self, key: int) -> None:
        self.array |= 1 << key

    def remove(self, key: int) -> None:
        self.array &= ~(1 << key)

    def contains(self, key: int) -> bool:
        return self.array & (1 << key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)