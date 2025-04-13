class Solution:
    mod = 10 ** 9 + 7
    def countGoodNumbers(self, n: int) -> int:
        return (
            self.fastPow(5, n // 2 + n % 2) \
            * self.fastPow(4, n // 2)
        ) % self.mod
    
    def fastPow(self, base: int, exp: int) -> int:
        result = 1
        while exp > 0:
            if exp % 2:
                result = (result * base) % self.mod
            base = (base * base) % self.mod
            exp //= 2
        return result

