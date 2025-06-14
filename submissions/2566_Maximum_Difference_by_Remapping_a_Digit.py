class Solution:
    def minMaxDifference(self, num: int) -> int:
        numStr = str(num)
        N = len(numStr)

        if numStr.count("9") == N:
            return num

        targetId = 0
        while numStr[targetId] == "9" and targetId < N:
            targetId += 1
        
        targetNum = numStr[targetId]
        maxNum = int(numStr.replace(targetNum, "9"))
        minNum = int(numStr.replace(numStr[0], "0"))

        return maxNum - minNum

