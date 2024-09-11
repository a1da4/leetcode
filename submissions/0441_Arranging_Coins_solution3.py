class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n

        while l <= r:
            m = (l + r) // 2
            t = m * (m + 1) // 2
            if t == n:
                return m
            elif t > n:
                r = m - 1
            else:
                l = m + 1
        
        return r

