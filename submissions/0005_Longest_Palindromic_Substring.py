class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        maxLen=1
        maxStr=s[0]
        for leftId in range(len(s)-1):
            for rightId in range(leftId+1,len(s)):
                if rightId-leftId+1 > maxLen and s[leftId:rightId+1] == s[leftId:rightId+1][::-1]:
                    maxLen = rightId-leftId+1
                    maxStr = s[leftId:rightId+1]

        return maxStr
