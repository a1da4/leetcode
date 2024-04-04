class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for n in range(1, len(s)//2 + 1):
            if s[:n] * (len(s)//n) == s:
                return True
        return False
