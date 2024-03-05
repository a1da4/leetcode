class Solution:
    def minimumLength(self, s: str) -> int:
        leftId = 0
        rightId = len(s) - 1
        while leftId < rightId and s[leftId] == s[rightId]:
            currChar = s[leftId]
            while leftId <= rightId and s[leftId] == currChar:
                leftId += 1
            while leftId <= rightId and s[rightId] == currChar:
                rightId -= 1

        return rightId - leftId + 1
