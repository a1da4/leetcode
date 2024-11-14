class Solution:
    def __init__(self):
        self.memo = {1: 1}

    def numTrees(self, n: int) -> int:
        if n not in self.memo:
            val = self.numTrees(n - 1) * 2 * (2 * (n - 1) + 1) // (n + 1)
            self.memo[n] = int(val)

        return self.memo[n]

