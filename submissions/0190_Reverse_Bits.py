class Solution:
    def reverseBits(self, n: int) -> int:
        nInvChar = bin(n)[::-1][:-2]
        while len(nInvChar) < 32:
            nInvChar += "0"
        return int(nInvChar, 2)
