class MovingAverage:

    def __init__(self, size: int):
        self.limit = size
        self._size = 0
        self._sum = 0
        self.queue = deque([])

    def next(self, val: int) -> float:
        self.queue.append(val)
        self._sum += val
        self._size += 1
        if self._size > self.limit:
            self._sum -= self.queue.popleft()
            self._size -= 1
        return self._sum / self._size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
