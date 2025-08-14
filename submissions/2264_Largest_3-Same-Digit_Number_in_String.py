class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for digit in range(9, -1, -1):
            target = str(digit) * 3
            if target in num:
                return target
        return ""
