class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        for num in num1:
            n1 = n1 * 10 + int(num)
        for num in num2:
            n2 = n2 * 10 + int(num)

        return str(n1 * n2)
