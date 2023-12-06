class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum([1 if bit == "1" else 0 for bit in str(bin(n)[2:])])
