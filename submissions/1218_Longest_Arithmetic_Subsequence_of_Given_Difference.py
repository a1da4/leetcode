class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        answer = 0

        for num in arr:
            dp[num] = dp[num - difference] + 1
            answer = max(answer, dp[num])

        return answer

