class Solution:
    def lengthAfterTransformations(
        self,
        s: str, 
        t: int,
    ) -> int:
        dp = [0] * 26
        mod = 10 ** 9 + 7
        ordA = ord('a')
        for ch in s:
            dp[ord(ch) - ordA] += 1

        for _ in range(t):
            temp = [0] * 26
            for i in range(25):
                temp[i + 1] = (
                    temp[i + 1] + dp[i]
                ) % mod
            temp[0] = (
                temp[0] + dp[25]
            ) % mod
            temp[1] = (
                temp[1] + dp[25]
            ) % mod
            dp = temp
        
        answer = 0
        for i in range(26):
            answer = (
                answer + dp[i]
            ) % mod

        return answer

