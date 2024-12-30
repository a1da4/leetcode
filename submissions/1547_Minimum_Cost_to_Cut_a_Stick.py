class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        memo = {}
        cuts = [0] + sorted(cuts) + [n]

        def search(left: int, right: int):
            if (left, right) in memo:
                return memo[(left, right)]
            if right - left == 1:
                return 0
            
            cost = min(search(left, mid) + search(mid, right) \
                        + cuts[right] - cuts[left] \
                        for mid in range(left + 1, right))
            
            memo[(left, right)] = cost
            return cost
        
        return search(0, len(cuts) - 1)

