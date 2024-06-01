class Solution:
    def scoreOfString(self, s: str) -> int:
        ords = [ord(ch) for ch in s]
        return sum([abs(ords[i] - ords[i + 1]) for i in range(len(ords) - 1)])
