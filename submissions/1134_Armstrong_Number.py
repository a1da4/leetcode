class Solution:
    def isArmstrong(self, n: int) -> bool:
        _n = n
        curr = 0
        k = int(log10(n)) + 1
        while _n > 0:
            digit = _n % 10
            _n -= digit
            _n /= 10
            curr += digit ** k
            if curr > n:
                return False
        return curr == n
