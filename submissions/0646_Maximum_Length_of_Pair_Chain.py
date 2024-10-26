class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        N = len(pairs)
        pairs.sort()
        chains = [1] * N
        for i in range(1, N):
            for j in range(i - 1, -1, -1):
                if pairs[j][1] < pairs[i][0]:
                    chains[i] += chains[j]
                    break

        return max(chains)

