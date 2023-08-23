class Solution:
    def numTilings(self, n: int) -> int:
        ways = [0] * n
        ways[0] = 1
        if n >= 2:
            ways[1] = 2
        if n >= 3:
            ways[2] = 5

        for i in range(3, n):
            ways[i] = (ways[i - 1] * 2 + ways[i - 3]) % 1000000007

        return ways[n - 1]
