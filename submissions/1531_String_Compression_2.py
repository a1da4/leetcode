class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        numChar = len(s)
        dp = [[float("inf")] * 110 for _ in range(110)]
        dp[0][0] = 0

        for currId in range(1, numChar + 1):
            for delId in range(k + 1):
                currCount = 0
                delCount = 0
                for nextId in range(currId, 0, -1):
                    if s[nextId - 1] == s[currId - 1]:
                        currCount += 1
                    else:
                        delCount += 1

                    if delId - delCount >= 0:
                        if currCount > 1:
                            num = int(math.log10(currCount)) + 1
                        else:
                            num = 0
                        dp[currId][delId] = min(dp[currId][delId], dp[nextId - 1][delId - delCount] + 1 + num)
                
                if delId > 0:
                    dp[currId][delId] = min(dp[currId][delId], dp[currId - 1][delId - 1])
        
        return dp[numChar][k]
