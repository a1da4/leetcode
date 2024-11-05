class Solution:
    def minChanges(self, s: str) -> int:
        answer = 0
        for i in range(0, len(s), 2):
            answer += (s[i] != s[i + 1])

        return answer

