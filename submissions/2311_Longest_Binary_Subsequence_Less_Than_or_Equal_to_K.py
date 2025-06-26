class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        answer = 0  
        curr = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                answer += 1
            else:
                weight = 1 << answer
                if curr + weight <= k:
                    curr += weight
                    answer += 1

        return answer
