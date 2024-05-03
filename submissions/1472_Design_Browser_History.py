class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.currId = 0

    def visit(self, url: str) -> None:
        if self.currId + 1 < len(self.history):
            self.currId += 1
            self.history[self.currId] = url
            self.history = self.history[:self.currId + 1]
        else:
            self.history.append(url)
            self.currId += 1 

    def back(self, steps: int) -> str:
        self.currId -= steps
        if self.currId < 0:
            self.currId = 0
        return self.history[self.currId]

    def forward(self, steps: int) -> str:
        self.currId += steps
        if self.currId >= len(self.history):
            self.currId = len(self.history) - 1
        return self.history[self.currId]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
