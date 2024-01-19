class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        size = 1
        start = 0
        for currId in range(1, len(s)):
            leftId = currId - size
            rightId = currId + 1
            sBig = s[leftId - 1:rightId]
            sSmall = s[leftId:rightId]
            if sBig == sBig[::-1] and len(sBig) > size:
                size += 2
                start = leftId - 1
            elif sSmall == sSmall[::-1] and len(sSmall) > size:
                size += 1
                start = leftId
        
        return s[start:start+size]
