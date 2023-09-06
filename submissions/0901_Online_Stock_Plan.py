class StockSpanner:

    def __init__(self):
        self.stack = []
        self.day = None

    def next(self, price: int) -> int:
        if self.day is None:
            self.day = 0
        else:
            self.day += 1

        if not self.stack or price < self.stack[-1][0]:
            self.stack.append((price, self.day))
            return 1
        else:
            while self.stack and price >= self.stack[-1][0]:
                _, _ = self.stack.pop()
            if len(self.stack) > 0:
                answer = self.day - self.stack[-1][1]
            else:
                answer = self.day + 1
            self.stack.append((price, self.day))
            return answer

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
