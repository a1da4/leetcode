class Solution:
    def __init__(self):
        self.note = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        if n not in self.note:         
            self.note[n] = self.fib(n - 1) + self.fib(n - 2)

        return self.note[n]

