class Solution:

    def __init__(self, w: List[int]):
        self._total = sum(w)
        self.N = len(w)
        self.w = [0] * self.N
        for i in range(self.N):
            self.w[i] = w[i] / self._total
            if i > 0:
                self.w[i] += self.w[i - 1]

    def pickIndex(self) -> int:
        prob = random.random()
        return bisect.bisect_right(self.w, prob)
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
