class Solution:
    def minLength(self, s: str) -> int:
        N = len(s)
        prev = float("inf")
        curr = N
        while curr != prev:
            prev = curr
            if "AB" in s:
                curr -= 2
                s = self.removeSubString(s, "AB")
            
            if "CD" in s:
                curr -= 2
                s = self.removeSubString(s, "CD")
        
        return curr

    def removeSubString(self, s: str, sub: str) -> str:
        targetId = None
        for i in range(len(s) - 1):
            if s[i:i+2] == sub:
                targetId = i
                break
        
        return s[:targetId] + s[targetId+2:]
