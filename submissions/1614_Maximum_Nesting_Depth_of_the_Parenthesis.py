class Solution:
    def maxDepth(self, s: str) -> int:
        currDepth = 0
        maxDepth = 0

        for ch in s:
            if ch == "(":
                currDepth += 1
                maxDepth = max(currDepth, maxDepth)
            if ch == ")":
                currDepth -= 1

        return maxDepth
