class Solution:
    def __init__(self):
        self.S = [0]
        for t in range(1, 61):
            self.S.append(
                self.S[-1] + ((t + 1) // 2) * (1 << (t - 1))
            )

    def get(self, num: int) -> int:
        if num <= 0:
            return 0
        k = num.bit_length()
        tail = num - (1 << (k - 1)) + 1
        return self.S[k - 1] + ((k + 1) // 2) * tail

    def minOperations(self, queries: list[list[int]]) -> int:
        res = 0
        for L, R in queries:
            T = self.get(R) - self.get(L - 1)
            res += (T + 1) // 2
        return res

