class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        xEven, yEven = int(n // 2), int(m // 2)
        xOdd, yOdd = n - xEven, m - yEven

        return xEven * yOdd + xOdd * yEven
