class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans = x
        ands = 1
        n -= 1
        while n > 0:
            if (ands & x) == 0:
                ans |= (n & 1) * ands
                n >>= 1
            ands <<= 1

        return ans

