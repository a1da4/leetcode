class Solution:
    def longestValidParentheses(self, s: str) -> int:
        answer = 0
        N = len(s)
        stack = [-1]
        for currId in range(N):
            if s[currId] == "(":
                stack.append(currId)
            else:
                stack.pop()
                if not stack:
                    stack.append(currId)
                else:
                    answer = max(answer, currId - stack[-1])
        return answer
