class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)
        tsum = [0]*n
        tsum[-1] = piles[-1]
        for i in range(n-2, -1, -1):
            tsum[i] = tsum[i+1] + piles[i]

        memo = {}

        def helper(m, i):
            if 2 * m >= n - i:
                return tsum[i]
            if i >= n: 
                return 0 
            if (m, i) in memo: 
                return memo[(m, i)]
            tmp = - float('inf')
            for j in range(1, 2*m+1):
                tmp = max(tmp, tsum[i] - helper(max(m,j), i+j))
            memo[(m, i)] = tmp 
            return memo[(m, i)]
        
        return helper(1, 0)

