class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        sBin, gBin = bin(start)[2:], bin(goal)[2:]
        sLen, gLen = len(sBin), len(gBin)

        if sLen > gLen:
            gBin = "0" * (sLen - gLen) + gBin
            gLen = sLen
        
        if sLen < gLen:
            sBin = "0" * (gLen - sLen) + sBin
            sLen = gLen

        return sum([s != b for s, b in zip(sBin, gBin)])

