class StringIterator:

    def __init__(self, compressedString: str):
        self.queue = deque([])
        _id = 0
        N = len(compressedString)
        while _id < N:
            char = compressedString[_id]
            num = 0
            _id += 1
            while _id < N:
                if compressedString[_id] in "1234567890":
                    num = num * 10 + int(compressedString[_id])
                    _id += 1
                else:
                    break
            self.queue.append((char, num))
        
        self.char, self.num = self.queue.popleft()

    def next(self) -> str:
        if self.num > 0:
            self.num -= 1
            return self.char
        else:
            if self.queue:
                self.char, self.num = self.queue.popleft()
                self.num -= 1
                return self.char
            else:
                return " "

    def hasNext(self) -> bool:
        return self.num > 0 or self.queue


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
