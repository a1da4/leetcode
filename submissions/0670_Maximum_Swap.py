class Solution:
    def maximumSwap(self, num: int) -> int:
        
        numStr = list(str(num))
        N = len(numStr)
        maxIds = [0] * N
        maxIds[N - 1] = N - 1

        for i in range(N - 2, -1, -1):
            if numStr[i] > numStr[maxIds[i + 1]]:
                maxIds[i] = i
            else:
                maxIds[i] = maxIds[i + 1]
        
        for i in range(N):
            if numStr[i] < numStr[maxIds[i]]:
                numStr[i], numStr[maxIds[i]] = \
                    numStr[maxIds[i]], numStr[i]

                return int("".join(numStr))
        
        return num

