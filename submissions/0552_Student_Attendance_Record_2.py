class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7
        memo = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]

        def search(currN: int, currA: int, currL: int):
            if currA >= 2 or currL >= 3:
                return 0
            if currN == 0:
                return 1
            if memo[currN][currA][currL] != -1:
                return memo[currN][currA][currL]
            
            currC = ((search(currN - 1, currA, 0) + \
                    search(currN - 1, currA + 1, 0)) % mod + \
                    search(currN - 1, currA, currL + 1)) % mod

            memo[currN][currA][currL] = currC
            return currC

        return search(n, 0, 0)

