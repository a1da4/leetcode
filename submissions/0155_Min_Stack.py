class MinStack:

    def __init__(self):
        self.nums = deque()
        self.minNum = float("inf")
        self.numItems = 0

    def push(self, val: int) -> None:
        self.nums.append(val)
        self.minNum = min(self.minNum, val)
        self.numItems += 1

    def pop(self) -> None:
        self.nums.pop()
        self.numItems -= 1
        if self.numItems > 0:
            self.minNum = min(self.nums)
        else:
            self.minNum = float("inf")

    def top(self) -> int:
        val = self.nums[-1]
        return val

    def getMin(self) -> int:
        return self.minNum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
