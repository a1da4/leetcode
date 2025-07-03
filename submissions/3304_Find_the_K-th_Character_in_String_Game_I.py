class Solution:
    def kthCharacter(self, k: int) -> str:
        def nextCh(s: str) -> str:
            if s == "z":
                return "a"
            else:
                return chr(ord(s) + 1)
        
        def nextStr(s: str) -> str:
            return ''.join([nextCh(ch) for ch in s])

        curr = "a"
        while len(curr) < k:

            curr += nextStr(curr)
            
        return curr[k - 1]

