class Solution:

    def __init__(self, w: List[int]):
        self._total = sum(w)
        self.w = [_w/self._total for _w in w]
        self.N = len(w)

    def pickIndex(self) -> int:
        prob = random.random()
        curr = 0
        for i in range(self.N):
            curr += self.w[i]
            if curr >= prob:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
