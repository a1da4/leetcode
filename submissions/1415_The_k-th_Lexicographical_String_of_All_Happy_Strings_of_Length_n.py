class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        happy_strings = []

        def backtrack(curr: str):
            if len(curr) == n:
                happy_strings.append(curr)
            
            if len(curr) < n:
                for ch in ["a", "b", "c"]:
                    if len(curr) > 0 and curr[-1] == ch:
                        continue
                    backtrack(curr + ch)
            
        backtrack("")
        
        if len(happy_strings) < k:
            return ""
        else:
            return sorted(happy_strings)[k - 1]

