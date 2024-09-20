class Solution:
    def shortestPalindrome(self, s: str) -> str:
        N = len(s)
        if N == 0:
            return s
        
        l = 0
        for r in range(N - 1, -1, -1):
            if s[l] == s[r]:
                l += 1
        
        if l == N:
            return s
        
        target = s[l:]
        targetReversed = target[::-1]

        return targetReversed + self.shortestPalindrome(s[:l]) + target

