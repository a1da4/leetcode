class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        num2trust = {i + 1: False for i in range(n)}
        num2trusted = {i + 1: 0 for i in range(n)}

        for a, b in trust:
            num2trust[a] = True
            num2trusted[b] += 1
        
        for i in range(1, n + 1):
            if num2trust[i] is False and num2trusted[i] == n - 1:
                return i

        return -1
