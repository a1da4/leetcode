class Solution:
    def threeCombinations(
        self,
        n: int,
    ) -> int:
        if n < 0:
            return 0
        return (n + 2) * (n + 1) // 2

    def distributeCandies(
        self, 
        n: int, 
        limit: int,
    ) -> int:
        answer = self.threeCombinations(n)

        oneExceeded = 3 * self.threeCombinations(n - limit - 1)
        twoExceeded = 3 * self.threeCombinations(n - 2 * (limit + 1))
        threeExceeded = self.threeCombinations(n - 3 * (limit + 1))

        return answer - (oneExceeded - twoExceeded + threeExceeded)

