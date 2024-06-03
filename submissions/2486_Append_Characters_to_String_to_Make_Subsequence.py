class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        tId = 0
        sId = 0
        S = len(s)
        T = len(t)
        while sId < S and tId < T:
            if s[sId] == t[tId]:
                tId += 1
            sId += 1
        return T - tId
