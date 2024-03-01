class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        N = len(s)
        n1 = Counter(s)["1"] - 1
        return "1" * n1 + "0" * (N - n1 - 1) + "1"

