class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        matchMat = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for rowId, char1 in enumerate(text1):
            for colId, char2 in enumerate(text2):
                if char1 == char2:
                    matchMat[rowId + 1][colId + 1] = matchMat[rowId][colId] + 1
                else:
                    matchMat[rowId + 1][colId + 1] = max(matchMat[rowId + 1][colId], matchMat[rowId][colId + 1])
        
        return matchMat[-1][-1]
