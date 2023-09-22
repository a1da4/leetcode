class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        
        hayLength = len(haystack)
        neeLength = len(needle)
        if hayLength < neeLength:
            return -1

        for start in range(hayLength - neeLength + 1):
            print(haystack[start:start+neeLength])
            if haystack[start:start+neeLength] == needle:
                return start
        
        return -1
