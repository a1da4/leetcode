class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num = n * (n + 1) // 2
        if n < m:
            return num
        
        M = n // m
        return num - m * (M * (M + 1))
