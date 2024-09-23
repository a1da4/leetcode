class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        N = len(s)
        vocab = set(dictionary)
        dp = [0] * (len(s) + 1)

        for start in range(N - 1, -1, -1):
            dp[start] = 1 + dp[start + 1]
            for end in range(start, N):
                curr = s[start: end + 1]
                if curr in vocab:
                    dp[start] = min(dp[start], dp[end + 1])

        return dp[0]

