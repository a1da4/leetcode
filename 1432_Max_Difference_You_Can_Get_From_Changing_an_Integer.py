class Solution:
    def maxDiff(self, num: int) -> int:
        numStr = str(num)
        N = len(numStr)
        for digit in range(1, 10):
            if numStr.count(str(digit)) == N:
                return int("8" * N)
            
        aId = 0
        while aId < N and numStr[aId] == "9":
            aId += 1
        
        a = int(numStr.replace(numStr[aId], "9"))

        if numStr[0] == "1":
            bId = 1
            while bId < N and numStr[bId] in {"0", "1"}:
                bId += 1
            
            if bId < N:
                b = int(numStr.replace(numStr[bId], "0"))
            else:
                b = num

        else:
            b = int(numStr.replace(numStr[0], "1"))
        
        return a - b
