class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.currSize = 0
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if self.currSize < self.maxSize:
            self.stack.append(x)
            self.currSize += 1

    def pop(self) -> int:
        if self.currSize > 0:
            self.currSize -= 1
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(self.currSize, k)):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
