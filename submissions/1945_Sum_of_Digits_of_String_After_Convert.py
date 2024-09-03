class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ord_a = ord("a")
        curr = 0
        for ch in s:
            ord_ch = (ord(ch) - ord_a + 1)
            curr += (ord_ch // 10) + (ord_ch % 10)

        for _ in range(k - 1):
            prev, curr = curr, 0
            while prev > 0:
                curr += prev % 10
                prev //= 10
    
        return curr

