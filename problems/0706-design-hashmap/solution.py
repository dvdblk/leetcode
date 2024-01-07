class MyHashMap:
    """via list (slow runtime due to initialization)"""

    def __init__(self):
        self.list = [-1] * int(10e6)

    def put(self, key: int, value: int) -> None:
        self.list[key] = value

    def get(self, key: int) -> int:
        return self.list[key]

    def remove(self, key: int) -> None:
        self.list[key] = -1

class MyHashMap:
    """via list (faster runtime because list is dynamic)"""

    def __init__(self):
        self.list = []

    def put(self, key: int, value: int) -> None:
        if key >= len(self.list):
            # adjust size of list if needed
            self.list += [-1] * (key - len(self.list) + 1)
        self.list[key] = value

    def get(self, key: int) -> int:
        if key >= len(self.list):
            return -1
        return self.list[key]

    def remove(self, key: int) -> None:
        if key < len(self.list):
            self.list[key] = -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)