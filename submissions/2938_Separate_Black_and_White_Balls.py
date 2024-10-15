class Solution:
    def minimumSteps(self, s: str) -> int:
        wPos = 0
        total = 0
        for cPos, char in enumerate(s):
            if char == "0":
                total += cPos - wPos
                wPos += 1

        return total

