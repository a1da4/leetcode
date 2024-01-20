class Solution:
    def longestValidParentheses(self, s: str) -> int:
        answer = 0
        currId = 0
        N = len(s)
        while currId < N:
            if s[currId] == ")":
                currId += 1
            else:
                leftParens = 1
                currLength = 0
                for nextId in range(currId+1, N):
                    paren = s[nextId]
                    if paren == "(":
                        leftParens += 1
                    else:
                        # paren == ")"
                        if leftParens > 0:
                            leftParens -= 1
                            if leftParens == 0:
                                currLength = nextId - currId + 1
                        else:
                            answer = max(answer, currLength)
                            currLength = 0
                            break
                answer = max(answer, currLength)
                currId += 1
        return answer
