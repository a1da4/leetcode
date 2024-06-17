class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(math.sqrt(c)) + 1):
            b = math.sqrt(c - a ** 2)
            if c == a ** 2 or b.is_integer():
                return True
        return False
