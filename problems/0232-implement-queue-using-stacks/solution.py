class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        # empty s1 into s2
        while self.s1:
            elem = self.s1.pop()
            self.s2.append(elem)

        # pop result
        res = self.s2.pop()
        while self.s2:
            elem = self.s2.pop()
            self.s1.append(elem)

        return res

    def peek(self) -> int:
        return self.s1[0]

    def empty(self) -> bool:
        return not self.s1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
