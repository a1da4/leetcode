class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n < 2:
            return n

        def finish(num: int):
            return num * (num + 1) // 2 > n
        
        for i in range(n):
            if finish(i + 1):
                return i

