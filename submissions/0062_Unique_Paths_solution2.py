class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m, n = n, m
        return math.comb(m + n - 2, n - 1)
