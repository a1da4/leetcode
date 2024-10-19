class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        s = "0"

        def rev(s: str) -> str:
            return s[::-1]
        
        def inv(s: str) -> str:
            n = len(s)
            _s = bin(int(s, 2) ^ int("1" * n, 2))[2:]
            _n = len(_s)
            if _n < n:
                _s = "0" * (n - _n) + _s
            return _s

        for i in range(n):
            s += "1" + rev(inv(s))
        
        return s[k - 1]
