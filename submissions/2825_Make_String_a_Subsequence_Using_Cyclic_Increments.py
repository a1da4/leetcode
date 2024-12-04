class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        N1, N2 = len(str1), len(str2)
        if N1 < N2:
            return False 

        ch2cands: Dict[str, Set[str]] = {}
        for i in range(ord("a"), ord("z")):
            ch2cands[chr(i)] = {chr(i), chr(i + 1)}
        ch2cands["z"] = {"z", "a"}

        id2 = 0
        
        for id1 in range(N1):
            ch = str1[id1]
            if str2[id2] in ch2cands[ch]:
                id2 += 1
                if id2 == N2:
                    return True
        
        return False
