class MyCircularDeque:

    def __init__(self, k: int):
        self.limit = k
        self.curr = 0
        self.queue = []

    def insertFront(self, value: int) -> bool:
        if self.curr < self.limit:
            self.queue = [value] + self.queue
            self.curr += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.curr < self.limit:
            self.queue.append(value)
            self.curr += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.curr > 0:
            self.queue.pop(0)
            self.curr -= 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.curr > 0:
            self.queue.pop(-1)
            self.curr -= 1
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.curr > 0:
            return self.queue[0]
        else:
            return -1

    def getRear(self) -> int:
        if self.curr > 0:
            return self.queue[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.curr == 0

    def isFull(self) -> bool:
        return self.curr == self.limit


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
